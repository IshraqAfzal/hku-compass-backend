from bson import ObjectId

def create_objectid(s):
  return ObjectId(str(s).encode("utf-8").hex().zfill(24))