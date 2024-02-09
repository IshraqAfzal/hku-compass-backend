subclasses_schema = {
  "properties": {
    "SUBCLASS_ID": {
      "bsonType": "objectId"
    },
    "COURSE_ID": {
      "bsonType": "objectId"
    },
    "STRM": {
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
    "SUBCLASS_CODE": {
      "bsonType": "string"
    },
    "TIMINGS": {
      "bsonType": "array",
      "items": {
        "bsonType": "object",
        "properties": {
          "DAY": {
            "bsonType": "string"
          },
          "VENUE": {
            "bsonType": "string"
          },
          "START_TIME": {
            "bsonType": "string"
          },
          "END_TIME": {
            "bsonType": "string"
          }
        }
      }
    }
  },
  "required": [
    "SUBCLASS_ID",
    "COURSE_ID",
    "SUBCLASS_CODE"
  ]
}
subclasses_validator = {
  "$jsonSchema" : subclasses_schema
}
