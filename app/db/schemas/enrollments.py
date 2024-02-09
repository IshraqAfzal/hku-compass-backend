enrollements_schema = {
  "properties": {
    "COURSE_ID": {
      "bsonType": "objectId"
    },
    "SUBCLASS_ID": {
      "bsonType": "string"
    },
    "QUOTA": {
      "bsonType": ["int", "null"]
    },
    "APPROVED_HEAD_COUNT": {
      "bsonType": ["int", "null"]
    }
  },
  "required": [
    "COURSE_ID",
    "SUBCLASS_ID"
  ]
}
enrollments_validator = {
  "$jsonSchema" : enrollements_schema
}
