from bson import ObjectId
from ..utils.datetime.random_date import random_date_last_six_months
import random

def generate_random_number(x, y):
  return float(random.randint(x, y))


mock_prof_reviews = [
  {
    "COURSE_CODE": "COMP3322",
    "USER_ID": ObjectId("5f94a577fcaee5e5f36dc0f1"),
    "PROF_ID": ObjectId("00000061746374616d5f6373"),
    "SUBLCASS_CODE": "COMP3322-2B",
    "COMMENT": "The professor's passion for the subject was evident, making the lectures both informative and enjoyable.",
    "ENGAGEMENT": generate_random_number(1, 5),
    "CLARITY": generate_random_number(1, 5),
    "DATETIME": random_date_last_six_months(),
    "YEAR": "2023-24",
    "SEM": "2",
    "IS_VERIFIED": True,
    "RATING": generate_random_number(1, 5),
    "HELPFUL": random.randint(5, 25),
    "NOT_HELPFUL": random.randint(5, 25),
  },
  {
    "COURSE_CODE": "COMP3322",
    "USER_ID": ObjectId("5f94a577fcaee5e5f36dc0f2"),
    "PROF_ID": ObjectId("00000061746374616d5f6373"),
    "SUBLCASS_CODE": "COMP3322-2B",
    "COMMENT": "Extremely helpful and approachable. Always available to clarify doubts and provide guidance outside of class.",
    "ENGAGEMENT": generate_random_number(1, 5),
    "CLARITY": generate_random_number(1, 5),
    "DATETIME": random_date_last_six_months(),
    "YEAR": "2023-24",
    "SEM": "2",
    "IS_VERIFIED": False,
    "RATING": generate_random_number(1, 5),
    "HELPFUL": random.randint(5, 25),
    "NOT_HELPFUL": random.randint(5, 25),
  },
  {
    "COURSE_CODE": "COMP3322",
    "USER_ID": ObjectId("5f94a577fcaee5e5f36dc0f3"),
    "PROF_ID": ObjectId("00000061746374616d5f6373"),
    "SUBLCASS_CODE": "COMP3322-2B",
    "COMMENT": "Amazing professor! Clearly explained complex concepts and kept the class engaged throughout.",
    "ENGAGEMENT": generate_random_number(1, 5),
    "CLARITY": generate_random_number(1, 5),
    "DATETIME": random_date_last_six_months(),
    "YEAR": "2023-24",
    "SEM": "2",
    "IS_VERIFIED": False,
    "RATING": generate_random_number(1, 5),
    "HELPFUL": random.randint(5, 25),
    "NOT_HELPFUL": random.randint(5, 25),
  },
  {
    "COURSE_CODE": "COMP3322",
    "USER_ID": ObjectId("5f94a577fcaee5e5f36dc0f4"),
    "PROF_ID": ObjectId("00000061746374616d5f6373"),
    "SUBLCASS_CODE": "COMP3322-2B",
    "COMMENT": "Lectures tended to be disorganized, which made it difficult to follow along and grasp the material.",
    "ENGAGEMENT": generate_random_number(1, 5),
    "CLARITY": generate_random_number(1, 5),
    "DATETIME": random_date_last_six_months(),
    "YEAR": "2023-24",
    "SEM": "2",
    "IS_VERIFIED": True,
    "RATING": generate_random_number(1, 5),
    "HELPFUL": random.randint(5, 25),
    "NOT_HELPFUL": random.randint(5, 25),
  },
  {
    "COURSE_CODE": "COMP3322",
    "USER_ID": ObjectId("5f94a577fcaee5e5f36dc0f5"),
    "PROF_ID": ObjectId("00000061746374616d5f6373"),
    "SUBLCASS_CODE": "COMP3322-2B",
    "COMMENT": "Received little feedback on assignments, making it challenging to gauge progress and improve.",
    "ENGAGEMENT": generate_random_number(1, 5),
    "CLARITY": generate_random_number(1, 5),
    "DATETIME": random_date_last_six_months(),
    "YEAR": "2023-24",
    "SEM": "2",
    "IS_VERIFIED": False,
    "RATING": generate_random_number(1, 5),
    "HELPFUL": random.randint(5, 25),
    "NOT_HELPFUL": random.randint(5, 25),
  },
  {
    "COURSE_CODE": "COMP3322",
    "USER_ID": ObjectId("5f94a577fcaee5e5f36dc0f6"),
    "PROF_ID": ObjectId("00000061746374616d5f6373"),
    "SUBLCASS_CODE": "COMP3322-2B",
    "COMMENT": "Not bad.",
    "ENGAGEMENT": generate_random_number(1, 5),
    "CLARITY": generate_random_number(1, 5),
    "DATETIME": random_date_last_six_months(),
    "YEAR": "2023-24",
    "SEM": "2",
    "IS_VERIFIED": True,
    "RATING": generate_random_number(1, 5),
    "HELPFUL": random.randint(5, 25),
    "NOT_HELPFUL": random.randint(5, 25),
  },
  {
    "COURSE_CODE": "COMP3322",
    "USER_ID": ObjectId("5f94a577fcaee5e5f36dc0f7"),
    "PROF_ID": ObjectId("00000061746374616d5f6373"),
    "SUBLCASS_CODE": "COMP3322-2B",
    "COMMENT": "Didn't like the professor.",
    "ENGAGEMENT": generate_random_number(1, 5),
    "CLARITY": generate_random_number(1, 5),
    "DATETIME": random_date_last_six_months(),
    "YEAR": "2023-24",
    "SEM": "2",
    "IS_VERIFIED": False,
    "RATING": generate_random_number(1, 5),
    "HELPFUL": random.randint(5, 25),
    "NOT_HELPFUL": random.randint(5, 25),
  },
  {
    "COURSE_CODE": "COMP3322",
    "USER_ID": ObjectId("5f94a577fcaee5e5f36dc0f8"),
    "PROF_ID": ObjectId("00000061746374616d5f6373"),
    "SUBLCASS_CODE": "COMP3322-2B",
    "COMMENT": "The professor was very thorough in his teaching.",
    "ENGAGEMENT": generate_random_number(1, 5),
    "CLARITY": generate_random_number(1, 5),
    "DATETIME": random_date_last_six_months(),
    "YEAR": "2023-24",
    "SEM": "2",
    "IS_VERIFIED": False,
    "RATING": generate_random_number(1, 5),
    "HELPFUL": random.randint(5, 25),
    "NOT_HELPFUL": random.randint(5, 25),
  }
]