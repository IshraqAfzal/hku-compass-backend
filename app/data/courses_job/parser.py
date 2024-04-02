import re, random
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
  try:
    for datum in data['mainTable']:
      course_id = datum['CRSE_ID']
      if course_id not in courses_obj:
        courses_obj[course_id] = {}
        history_obj[course_id] = {}
        courses_obj[course_id]['COURSE_ID'] = create_objectid(course_id)
        history_obj[course_id]['COURSE_ID'] = create_objectid(course_id)
        courses_obj[course_id]['CRSE_ID'] = str(course_id)
        history_obj[course_id]['CRSE_ID'] = str(course_id)
        courses_obj[course_id]['TNL'] = []
      courses_obj[course_id]['STRM'] = datum['STRM']
      history_obj[course_id]['STRM'] = datum['STRM']
      courses_obj[course_id]['COURSE_CODE'] = datum['SUBJECT_AREA'] + datum['CATALOG_NBR']
      history_obj[course_id]['COURSE_CODE'] = datum['SUBJECT_AREA'] + datum['CATALOG_NBR']
      courses_obj[course_id]['SUBJECT_AREA'] = datum['SUBJECT_AREA']
      courses_obj[course_id]['CATALOG_NUMBER'] = datum['CATALOG_NBR']
      courses_obj[course_id]['COURSE_TITLE'] = datum['COURSE_TITLE_LONG']
      courses_obj[course_id]['CREDITS'] = int(datum['CRSE_UNITS']) if datum['CRSE_UNITS'] is not None else None
      courses_obj[course_id]['ACAD_GROUP'] = datum['ACAD_GROUP']
      courses_obj[course_id]['FACULTY'] = datum['FACULTY_DESC']
      courses_obj[course_id]['INSTRUCTORS_PLACEHOLDER'] = datum['INSTRUCTOR_DISP']
      courses_obj[course_id]['ENROLLMENT_REQUIREMENTS'] = datum['ENROLLMENT_REQUIREMENTS']
      courses_obj[course_id]['ENROLLMENT_REQ_COURSES'] = []
      courses_obj[course_id]['RATING'] = generate_random_number(0,5)
      courses_obj[course_id]['USEFULNESS'] = generate_random_number(0,5)
      courses_obj[course_id]['GRADING'] = generate_random_number(0,5)
      courses_obj[course_id]['WORKLOAD'] = generate_random_number(0,5)
      courses_obj[course_id]['DIFFICULTY'] = generate_random_number(0,5)
      if datum['ENROLLMENT_REQUIREMENTS'] is not None:
        courses_obj[course_id]['ENROLLMENT_REQ_COURSES'] = re.compile(r'\b[A-Z]{4}\d{4}\b').findall(datum['ENROLLMENT_REQUIREMENTS'])
      courses_obj[course_id]['COURSE_DESCRIPTION'] = datum['COURSE_DESCRIPTION']
      enrollments.append({
        "COURSE_ID" : create_objectid(course_id),
        "SUBCLASS_ID" : datum['COURSE_SUBCLASS'],
        "QOUTA" : datum['CLASS_QUOTA'],
        "APPROVED_HEAD_COUNT" : datum['APPROVED_HEAD_CNT']
      })
  except Exception as ex:
    logger.error(ex)

  try:
    for datum in data['patterns']:
      course_id = datum['crse_id']
      sub_id = datum['course_subclass']
      if sub_id not in subclasses_obj:
        subclasses_obj[sub_id] = {}
        subclasses_obj[sub_id]['COURSE_ID'] = create_objectid(course_id)
        subclasses_obj[sub_id]['SUBCLASS_ID'] = create_objectid(sub_id)
        subclasses_obj[sub_id]['TIMINGS'] = []
      subclasses_obj[sub_id]['STRM'] = datum['strm']
      subclasses_obj[sub_id]['SUBCLASS_CODE'] = datum['course_subclass'][-2:]
      subclasses_obj[sub_id]['TIMINGS'].append({
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
          "COURSE_ID" : create_objectid(course_code),
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
        courses_obj[course_code]['TNL'].append({
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
