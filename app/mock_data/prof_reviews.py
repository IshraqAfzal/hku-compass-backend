from bson import ObjectId
from ..utils.datetime.hk_time_now import hk_time_now

mock_prof_reviews = [
  {
    "COURSE_CODE": "COMP3322",
    "USER_ID": ObjectId("5f94a577fcaee5e5f36dc0f1"),
    "PROF_ID": ObjectId("00000061746374616d5f6373"),
    "SUBLCASS_CODE": "COMP3322-2B",
    "COMMENT": "The professor's passion for the subject was evident, making the lectures both informative and enjoyable.",
    "ENGAGEMENT": 4.5,
    "CLARITY": 4.0,
    "DATETIME": hk_time_now(),
    "YEAR": "2023-24",
    "SEM": "2",
    "IS_VERIFIED": True,
    "RATING": 5.0,
    "HELPFUL": 10,
    "NOT_HELPFUL": 2
  },
  {
    "COURSE_CODE": "COMP3322",
    "USER_ID": ObjectId("5f94a577fcaee5e5f36dc0f2"),
    "PROF_ID": ObjectId("00000061746374616d5f6373"),
    "SUBLCASS_CODE": "COMP3322-2B",
    "COMMENT": "Extremely helpful and approachable. Always available to clarify doubts and provide guidance outside of class.",
    "ENGAGEMENT": 4.5,
    "CLARITY": 4.0,
    "DATETIME": hk_time_now(),
    "YEAR": "2023-24",
    "SEM": "2",
    "IS_VERIFIED": True,
    "RATING": 5.0,
    "HELPFUL": 10,
    "NOT_HELPFUL": 2
  },
  {
    "COURSE_CODE": "COMP3322",
    "USER_ID": ObjectId("5f94a577fcaee5e5f36dc0f3"),
    "PROF_ID": ObjectId("00000061746374616d5f6373"),
    "SUBLCASS_CODE": "COMP3322-2B",
    "COMMENT": "Amazing professor! Clearly explained complex concepts and kept the class engaged throughout.",
    "ENGAGEMENT": 4.5,
    "CLARITY": 4.0,
    "DATETIME": hk_time_now(),
    "YEAR": "2023-24",
    "SEM": "2",
    "IS_VERIFIED": True,
    "RATING": 5.0,
    "HELPFUL": 10,
    "NOT_HELPFUL": 2
  },
  {
    "COURSE_CODE": "COMP3322",
    "USER_ID": ObjectId("5f94a577fcaee5e5f36dc0f4"),
    "PROF_ID": ObjectId("00000061746374616d5f6373"),
    "SUBLCASS_CODE": "COMP3322-2B",
    "COMMENT": "Lectures tended to be disorganized, which made it difficult to follow along and grasp the material.",
    "ENGAGEMENT": 4.5,
    "CLARITY": 4.0,
    "DATETIME": hk_time_now(),
    "YEAR": "2023-24",
    "SEM": "2",
    "IS_VERIFIED": True,
    "RATING": 5.0,
    "HELPFUL": 10,
    "NOT_HELPFUL": 2
  },
  {
    "COURSE_CODE": "COMP3322",
    "USER_ID": ObjectId("5f94a577fcaee5e5f36dc0f5"),
    "PROF_ID": ObjectId("00000061746374616d5f6373"),
    "SUBLCASS_CODE": "COMP3322-2B",
    "COMMENT": "Received little feedback on assignments, making it challenging to gauge progress and improve.",
    "ENGAGEMENT": 4.5,
    "CLARITY": 4.0,
    "DATETIME": hk_time_now(),
    "YEAR": "2023-24",
    "SEM": "2",
    "IS_VERIFIED": True,
    "RATING": 5.0,
    "HELPFUL": 10,
    "NOT_HELPFUL": 2
  },
  {
    "COURSE_CODE": "COMP3322",
    "USER_ID": ObjectId("5f94a577fcaee5e5f36dc0f6"),
    "PROF_ID": ObjectId("00000061746374616d5f6373"),
    "SUBLCASS_CODE": "COMP3322-2B",
    "COMMENT": "Not bad.",
    "ENGAGEMENT": 4.5,
    "CLARITY": 4.0,
    "DATETIME": hk_time_now(),
    "YEAR": "2023-24",
    "SEM": "2",
    "IS_VERIFIED": True,
    "RATING": 5.0,
    "HELPFUL": 10,
    "NOT_HELPFUL": 2
  },
  {
    "COURSE_CODE": "COMP3322",
    "USER_ID": ObjectId("5f94a577fcaee5e5f36dc0f7"),
    "PROF_ID": ObjectId("00000061746374616d5f6373"),
    "SUBLCASS_CODE": "COMP3322-2B",
    "COMMENT": "Didn't like the professor.",
    "ENGAGEMENT": 4.5,
    "CLARITY": 4.0,
    "DATETIME": hk_time_now(),
    "YEAR": "2023-24",
    "SEM": "2",
    "IS_VERIFIED": True,
    "RATING": 5.0,
    "HELPFUL": 10,
    "NOT_HELPFUL": 2
  },
  {
    "COURSE_CODE": "COMP3322",
    "USER_ID": ObjectId("5f94a577fcaee5e5f36dc0f8"),
    "PROF_ID": ObjectId("00000061746374616d5f6373"),
    "SUBLCASS_CODE": "COMP3322-2B",
    "COMMENT": "INVEST IN BITCOIN NOW! Don't waste your time with professors, invest in your future with cryptocurrency! Click here for more info!",
    "ENGAGEMENT": 4.5,
    "CLARITY": 4.0,
    "DATETIME": hk_time_now(),
    "YEAR": "2023-24",
    "SEM": "2",
    "IS_VERIFIED": True,
    "RATING": 5.0,
    "HELPFUL": 10,
    "NOT_HELPFUL": 2
  }
]