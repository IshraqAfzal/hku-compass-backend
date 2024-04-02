course_reviews_schema = {
  "properties": {
    "COURSE_ID": {
      "bsonType": "objectId"
    },
    "USER_ID": {
      "bsonType": "objectId"
    },
    "PROF_IDS": {
      "bsonType": "array",
      "items": {
        "bsonType": "objectId"
      }
    },
    "COMMENT": {
      "bsonType": "string"
    },
    "RATING": {
      "bsonType": "int"
    },
    "USEFULNESS": {
      "bsonType": "double"
    },
    "WORKLOAD": {
      "bsonType": "double"
    },
    "GRADING": {
      "bsonType": "double"
    },
    "DIFFICULTY": {
      "bsonType": "double"
    },
    "DATETIME": {
      "bsonType": "date"
    },
    "IS_VERIFIED": {
      "bsonType": "bool"
    },
    "YEAR": {
      "bsonType": "string"
    },
    "SEM": {
      "bsonType": "string"
    },
    "HELPFUL": {
      "bsonType": "int"
    },
    "HELPFUL_USERS": {
      "bsonType": "array",
      "items": {
        "bsonType": "objectId"
      }
    },
    "NOT_HELPFUL": {
      "bsonType": "int"
    },
    "NOT_HELPFUL_USERS": {
      "bsonType": "array",
      "items": {
        "bsonType": "objectId"
      }
    },
  },
  "required": [
    "COURSE_ID",
    "USER_ID",
    "PROF_IDS",
    "USEFULNESS",
    "WORKLOAD",
    "GRADING",
    "DIFFICULTY",
    "DATETIME"
  ]
}
course_reviews_validator = {
  "$jsonSchema" : course_reviews_schema
}
