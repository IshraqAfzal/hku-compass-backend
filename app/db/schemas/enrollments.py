enrollments_schema = {
  "properties": {
    "COURSE_ID": {
      "bsonType": "objectId"
    },
    "SUBCLASS_ID": {
      "bsonType": "objectId"
    },
    "QUOTA": {
      "bsonType": ["int", "null"]
    },
    "APPROVED_HEAD_COUNT": {
      "bsonType": ["int", "null"]
    },
    "LAST_UPDATED": {
      "bsonType": "date"
    },
  },
  "required": [
    "COURSE_ID",
    "SUBCLASS_ID"
  ]
}
enrollments_validator = {
  "$jsonSchema" : enrollments_schema
}
