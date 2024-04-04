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
    "COMMENT": {
      "bsonType": "string"
    },
    "ENGAGEMENT": {
      "bsonType": "double"
    },
    "CLARITY": {
      "bsonType": "double"
    },
    "DATETIME": {
      "bsonType": "date"
    },
    "YEAR": {
      "bsonType": "string"
    },
    "SEM": {
      "bsonType": "string"
    },
    "IS_VERIFIED": {
      "bsonType": "bool"
    },
    "RATING": {
      "bsonType": "int"
    },
    "HELPFUL": {
      "bsonType": "int"
    },
    "NOT_HELPFUL": {
      "bsonType": "int"
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
