professors_schema = {
  "title": "professors",
  "bsonType": "object",
  "properties": {
    "title": {
      "bsonType": "string"
    },
    "firstname": {
      "bsonType": "string"
    },
    "lastname": {
      "bsonType": "string"
    },
    "faculty": {
      "bsonType": "string"
    },
    "department": {
      "bsonType": "string"
    },
    "email": {
      "bsonType": "string"
    },
    "courses": {
      "bsonType": "array",
      "items": {
        "bsonType": "string"
      }
    },
    "reviews": {
      "bsonType": "array",
      "items": {
        "bsonType": "objectId"
      }
    },
    "profileLink": {
      "bsonType": "string"
    }
  },
  "required": [
    "firstname",
    "lastname",
    "faculty",
    "department",
    "email",
    "profileLink"
  ]
}
professors_validator = {
  "$jsonSchema" : professors_schema
}
