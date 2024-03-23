sftl_schema = {
  "properties": {
    "COURSE_ID": {
      "bsonType": "objectId"
    },
    "STRM": {
      "bsonType": "string"
    },
    "YEAR": {
      "bsonType": "string"
    },
    "SEM": {
      "bsonType": "string"
    },
    "ENROLLMENT": {
      "bsonType": "int"
    },
    "RESPONSE": {
      "bsonType": "int"
    },
    "RESPONSE_RATE": {
      "bsonType": "int"
    },
    "MEAN": {
      "bsonType": "string"
    }
  },
  "required": [
    "COURSE_ID"
  ]
}
sftl_validator = {
  "$jsonSchema" : sftl_schema
}
