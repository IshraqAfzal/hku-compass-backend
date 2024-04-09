import re, random, datetime
from ...utils.data.create_objectid import create_objectid
from ...utils.data.strm import decode_strm

def generate_random_number(x, y):
  return float(random.randint(x, y))

def parse_json(data, logger):
  courses_obj = {}
  courses = []
  subclasses_obj = {}
  subclasses = []
  sftl = []
  enrollments = []
  history_obj = {}
  history = []
  id_to_code_map = {}
  try:
    for datum in data['mainTable']:
      course_code = datum['SUBJECT_AREA'] + datum['CATALOG_NBR']
      sub_code = datum['COURSE_SUBCLASS']
      if course_code not in courses_obj:
        courses_obj[course_code] = {}
        history_obj[course_code] = {}
        courses_obj[course_code]['COURSE_CODE'] = course_code
        history_obj[course_code]['COURSE_CODE'] = course_code
        id_to_code_map[datum["CRSE_ID"]] = course_code
        # courses_obj[course_code]['COURSE_ID'] = create_objectid(course_code)
        # history_obj[course_code]['COURSE_ID'] = create_objectid(course_code)
        # courses_obj[course_code]['CRSE_ID'] = str(course_code)
        # history_obj[course_code]['CRSE_ID'] = str(course_code)
        courses_obj[course_code]['TNL'] = []
      if sub_code not in subclasses_obj:
        subclasses_obj[sub_code] = {}
        # subclasses_obj[sub_code]['COURSE_ID'] = create_objectid(course_code)
        # subclasses_obj[sub_code]['SUBCLASS_ID'] = create_objectid(sub_code)
        subclasses_obj[sub_code]['COURSE_CODE'] = course_code
        subclasses_obj[sub_code]['SUBCLASS_CODE'] = sub_code
        subclasses_obj[sub_code]['TIMINGS'] = []
      # courses_obj[course_code]['STRM'] = datum['STRM']
      history_obj[course_code]['STRM'] = datum['STRM']
      history_obj[course_code]['YEAR'] = decode_strm(datum['STRM'])[0]
      history_obj[course_code]['SEM'] = decode_strm(datum['STRM'])[1]
      # courses_obj[course_code]['COURSE_CODE'] = datum['SUBJECT_AREA'] + datum['CATALOG_NBR']
      # history_obj[course_code]['COURSE_CODE'] = datum['SUBJECT_AREA'] + datum['CATALOG_NBR']
      # courses_obj[course_code]['SUBJECT_AREA'] = datum['SUBJECT_AREA']
      # courses_obj[course_code]['CATALOG_NUMBER'] = datum['CATALOG_NBR']
      courses_obj[course_code]['COURSE_TITLE'] = datum['COURSE_TITLE_LONG']
      courses_obj[course_code]['CREDITS'] = int(datum['CRSE_UNITS']) if datum['CRSE_UNITS'] is not None else None
      # courses_obj[course_code]['ACAD_GROUP'] = datum['ACAD_GROUP']
      courses_obj[course_code]['FACULTY'] = datum['FACULTY_DESC']
      history_obj[course_code]['INSTRUCTORS_PLACEHOLDER'] = datum['INSTRUCTOR_DISP']
      subclasses_obj[sub_code]['INSTRUCTORS_PLACEHOLDER'] = datum['INSTRUCTOR_DISP']
      courses_obj[course_code]['ENROLLMENT_REQUIREMENTS'] = datum['ENROLLMENT_REQUIREMENTS']
      # courses_obj[course_code]['ENROLLMENT_REQ_COURSES'] = []
      # TODO: rename the fields
      courses_obj[course_code]['RATING_COUNT'] = random.randint(10, 100)
      courses_obj[course_code]['RATING'] = generate_random_number(1,5) * courses_obj[course_code]['RATING_COUNT']
      courses_obj[course_code]['USEFULNESS'] = generate_random_number(1,5) * courses_obj[course_code]['RATING_COUNT']
      courses_obj[course_code]['GRADING'] = generate_random_number(1,5) * courses_obj[course_code]['RATING_COUNT']
      courses_obj[course_code]['WORKLOAD'] = generate_random_number(1,5) * courses_obj[course_code]['RATING_COUNT']
      courses_obj[course_code]['DIFFICULTY'] = generate_random_number(1,5) * courses_obj[course_code]['RATING_COUNT']
      # if datum['ENROLLMENT_REQUIREMENTS'] is not None:
      #   courses_obj[course_code]['ENROLLMENT_REQ_COURSES'] = re.compile(r'\b[A-Z]{4}\d{4}\b').findall(datum['ENROLLMENT_REQUIREMENTS'])
      courses_obj[course_code]['COURSE_DESCRIPTION'] = datum['COURSE_DESCRIPTION']
      enrollments.append({
        "COURSE_CODE" : course_code,
        "SUBCLASS_CODE" : sub_code,
        "QUOTA" : datum['CLASS_QUOTA'],
        "APPROVED_HEAD_COUNT" : datum['APPROVED_HEAD_CNT'],
        "LAST_UPDATED" : datetime.datetime.now()
      })
  except Exception as ex:
    logger.error(ex)

  try:
    for datum in data['patterns']:
      # course_code = datum['crse_id']
      sub_code = datum['course_subclass']
      # if sub_id not in subclasses_obj:
      #   subclasses_obj[sub_id] = {}
      #   subclasses_obj[sub_id]['COURSE_ID'] = create_objectid(course_id)
      #   subclasses_obj[sub_id]['SUBCLASS_ID'] = create_objectid(sub_id)
      #   subclasses_obj[sub_id]['TIMINGS'] = []
      # subclasses_obj[sub_code]['STRM'] = datum['strm']
      subclasses_obj[sub_code]['YEAR'] = decode_strm(datum['strm'])[0]
      subclasses_obj[sub_code]['SEM'] = decode_strm(datum['strm'])[1]
      subclasses_obj[sub_code]['SUBCLASS'] = datum['course_subclass'].split("-")[-1]
      subclasses_obj[sub_code]['TIMINGS'].append({
        'DAY': datum['day_str'],
        'START_TIME': datum['stime'],
        'END_TIME': datum['etime'],
        'VENUE': datum['descr'],
      })
  except Exception as ex:
    logger.error(ex)

  try:
    for course_code in data['setl']:
      for s in data['setl'][course_code]:
        sftl.append({
          "COURSE_CODE" : id_to_code_map[course_code],
          "YEAR" : s['acad_year'],
          "STRM" : s['strm'],
          "YEAR" : decode_strm(s['strm'])[0],
          "SEM" : decode_strm(s['strm'])[1],
          "ENROLLMENT" : s['enrollment'],
          "RESPONSE" : s['response'],
          "RESPONSE_RATE" : s['response_rate'],
          "MEAN" : s['mean'].strip(),
        })
  except Exception as ex:
    logger.error(ex)

  try:
    for course_code in data['teachingLearning']:
      for tnl in data['teachingLearning'][course_code]:
        courses_obj[id_to_code_map[course_code]]['TNL'].append({
          "DETAIL" : tnl['z_details'],
          "SHARE" : float(tnl['max_amount']),
          "PERCENTAGE" : float(tnl['z_max_amount']),
        })
  except Exception as ex:
    logger.error(ex)

  for course in courses_obj:
    courses.append(courses_obj[course])

  for his in history_obj:
    history.append(history_obj[his])

  for sub in subclasses_obj:
    subclasses.append(subclasses_obj[sub])

  return (courses, subclasses, sftl, enrollments, history)
