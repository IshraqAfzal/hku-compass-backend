import pandas as pd
import pathlib

def get_all_courses():
  df = pd.read_excel(str(pathlib.Path().resolve()) + "/data/files/2023-24_class_timetable_20230824.xlsx")
  hash = {}
  
  for i, row in df.iterrows():
    sem = int(row["TERM"].strip()[-1])
    career = row["ACAD_CAREER"]
    code  = row["COURSE CODE"]
    subclass_code = row["CLASS SECTION"]
    day = None
    if not pd.isnull(row["MON"]):
      day = "MON"
    elif not pd.isnull(row["TUE"]):
      day = "TUE"
    elif not pd.isnull(row["WED"]):
      day = "WED"
    elif not pd.isnull(row["THU"]):
      day = "THU"
    elif not pd.isnull(row["FRI"]):
      day = "FRI"
    # venue = row["VENUE"]
    start_time = row["START TIME"]
    end_time = row["END TIME"]
    title = row["COURSE TITLE"]
    dept = row["OFFER DEPT"]
    if code not in hash:
      hash[code] = {}
      hash[code]["code"] = code
      hash[code]["career"] = career
      hash[code]["title"] = title
      hash[code]["department"] = dept
      hash[code]["subclasses_obj"] = {}
    if subclass_code not in hash[code]["subclasses_obj"]:
      hash[code]["subclasses_obj"][subclass_code] = []
    if (sem, day, start_time, end_time) not in hash[code]["subclasses_obj"][subclass_code]:
      hash[code]["subclasses_obj"][subclass_code].append((sem, day, start_time, end_time))

  ans = []
  for code in hash:
    course = hash[code]
    ans_obj = course
    ans_obj["subclasses"] = []
    for subclass_code in course['subclasses_obj']:
      subclass = course["subclasses_obj"][subclass_code]
      ans_sub_obj = {}
      ans_sub_obj["code"] = subclass_code
      ans_sub_obj["sem"] = subclass[0][0]
      ans_sub_obj["timeslots"] = []
      for timing in subclass:
        timeslot = {}
        timeslot["day"] = timing[1]
        # timeslot["venue"] = timing[2]
        timeslot["startTime"] = timing[2]
        timeslot["endTime"] = timing[3]
        ans_sub_obj["timeslots"].append(timeslot)
      ans_obj["subclasses"].append(ans_sub_obj)
    del ans_obj['subclasses_obj']
    ans.append(ans_obj)
  return ans



