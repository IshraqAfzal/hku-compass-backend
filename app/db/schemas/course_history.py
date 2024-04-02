course_history_schema = {
  "properties": {
    "COURSE_ID": {
      "bsonType": "objectId"
    },
    "CRSE_ID": {
      "bsonType": "string"
    },
    "STRM": {
      "bsonType": "string"
    },
    "COURSE_CODE": {
      "bsonType": "string"
    },
    "INSTRUCTORS": {
      "bsonType": "array",
      "items": {
        "bsonType": "objectId"
      }
    }
  },
  "required": [
    "COURSE_ID",
    "STRM",
    "COURSE_CODE"
  ]
}
course_history_validator = {
  "$jsonSchema" : course_history_schema
}
