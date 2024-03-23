users_schema = {
  "properties": {
    "USER_ID": {
      "bsonType": "objectId"
    },
    "EMAIL": {
      "bsonType": "string"
    },
    "FULLNAME": {
      "bsonType": "string"
    },
    "DEPARTMENT": {
      "bsonType": ['null', "string"]
    },
    "FACULTY": {
      "bsonType": "string"
    },
    "MAJORS": {
      "bsonType": "array",
      "items": {
        "bsonType": "string"
      }
    },
    "MINORS": {
      "bsonType": "array",
      "items": {
        "bsonType": "string"
      }
    },
    "DEGREE": {
      "bsonType": "string"
    }, 
    "COURSE_HISTORY": {
      "bsonType": "array",
      "items": {
        "bsonType": "string"
      }
    },
    "BOOKMARKS": {
      "bsonType": "array",
      "items": {
        "bsonType": "string"
      }
    },
    "CART": {
      "bsonType": "array",
      "items": {
        "bsonType": "string"
      }
    }
  },
  "required": [
    "USER_ID",
    "EMAIL",
    "FULLNAME"
  ]
}
users_validator = {
  "$jsonSchema" : users_schema
}
