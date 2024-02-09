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
      "bsonType": "string"
    },
    "COURSES_COMPLETED": {
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
