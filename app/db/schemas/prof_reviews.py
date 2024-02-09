prof_reviews_schema = {
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
    "SUBLCASS_CODE": {
      "bsonType": "string"
    },
    "COMMENT": {
      "bsonType": "string"
    },
    "ENGAGEMENT": {
      "bsonType": "int"
    },
    "CLARITY": {
      "bsonType": "int"
    },
    "VALIDATED": {
      "bsonType": "bool"
    },
    "DATETIME": {
      "bsonType": "date"
    }
  },
  "required": [
    "COURSE_ID",
    "USER_ID",
    "PROF_ID",
    "ENGAGEMENT",
    "CLARITY",
    "DATETIME"
  ]
}
prof_reviews_validator = {
  "$jsonSchema" : prof_reviews_schema
}
