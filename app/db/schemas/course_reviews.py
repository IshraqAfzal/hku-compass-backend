course_reviews_schema = {
  "properties": {
    "COURSE_ID": {
      "bsonType": "objectId"
    },
    "USER_ID": {
      "bsonType": "objectId"
    },
    "PROF_ID": {
      "bsonType": "objectId"
    },
    "SUBCLASS_CODE": {
      "bsonType": "string"
    },
    "COMMENT": {
      "bsonType": "string"
    },
    "USEFULNESS": {
      "bsonType": "int"
    },
    "WORKLOAD": {
      "bsonType": "int"
    },
    "GRADING": {
      "bsonType": "int"
    },
    "DIFFICULTY": {
      "bsonType": "int"
    },
    "DATETIME": {
      "bsonType": "date"
    },
    "VALIDATED": {
      "bsonType": "bool"
    }
  },
  "required": [
    "COURSE_ID",
    "USER_ID",
    "PROF_ID",
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
