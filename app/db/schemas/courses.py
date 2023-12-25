courses_schema = {
  "properties": {
    "code": {
      "bsonType": "string"
    },
    "career": {
      "bsonType": "string"
    },
    "title": {
      "bsonType": "string"
    },
    "department": {
      "bsonType": "string"
    },
    "faculty": {
      "bsonType": "string"
    },
    "description": {
      "bsonType": "string"
    },
    "credit": {
      "bsonType": "int"
    },
    "subclasses": {
      "bsonType": "array",
      "items": {
        "bsonType": "object",
        "properties": {
          "code": {
            "bsonType": "string"
          },
          "sem": {
            "bsonType": "int"
          },
          "profId": {
            "bsonType": "objectId"
          },
          "timeslots": {
            "bsonType": "array",
            "items": {
              "bsonType": "object",
              "properties": {
                "day": {
                  "bsonType": "string"
                },
                "startTime": {
                  "bsonType": "string"
                },
                "endTime": {
                  "bsonType": "string"
                }
              }
            }
          }
        }
      }
    },
    "profIds": {
      "bsonType": "array",
      "items": {
        "bsonType": "objectId"
      }
    },
    "reviews": {
      "bsonType": "array",
      "items": {
        "bsonType": "objectId"
      }
    }
  },
  "required": [
    "code"
  ]
}
courses_validator = {
  "$jsonSchema" : courses_schema
}
