courses_schema = {
  "properties": {
    "COURSE_ID": {
      "bsonType": "objectId"
    },
    "STRM": {
      "bsonType": "string"
    },
    "COURSE_CODE": {
      "bsonType": "string"
    },
    "COURSE_TITLE": {
      "bsonType": "string"
    },
    "CREDITS": {
      "bsonType": "int"
    },
    "SUBJECT_AREA": {
      "bsonType": "string"
    },
    "CATALOG_NUMBER": {
      "bsonType": "string"
    },
    "ACAD_GROUP": {
      "bsonType": "string"
    },
    "FACULTY": {
      "bsonType": "string"
    },
    "INSTRUCTORS": {
      "bsonType": "array",
      "items": {
        "bsonType": "objectId"
      }
    },
    "INSTRUCTORS_PLACEHOLDER": {
      "bsonType": "string",
    },
    "ENROLLMENT_REQUIREMENTS": {
      "bsonType": [ "null", "string" ]
    },
    "ENROLLMENT_REQ_COURSES": {
      "bsonType": "array",
      "items": {
        "bsonType": "string"
      }
    },
    "COURSE_DESCRIPTION": {
      "bsonType": "string"
    },"USEFULNESS": {
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
    "TNL": {
      "bsonType": "array",
      "items": {
        "bsonType": "object",
        "properties": {
          "DETAIL": {
            "bsonType": "string"
          },
          "SHARE": {
            "bsonType": "double"
          },
          "PERCENTAGE": {
            "bsonType": "double"
          }
        }
      }
    }
  },
  "required": [
    "COURSE_ID",
    "STRM",
    "COURSE_CODE",
    "COURSE_TITLE"
  ]
}
courses_validator = {
  "$jsonSchema" : courses_schema
}
