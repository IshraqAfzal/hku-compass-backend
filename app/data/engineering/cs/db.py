from pymongo import ReplaceOne

def write(db, logger, data):
  profs = data["profs"]
  profs_insertion_list = map_insertion_list(prof_replace_obj, profs)
  db.bulk_write("professors", profs_insertion_list)

def map_insertion_list(mapper, list):
  mapped_list = []
  for l in list:
    mapped_list.append(mapper(l))
  return mapped_list

def prof_replace_obj(prof):
  return ReplaceOne({"profileLink" : prof["profileLink"]}, prof, upsert=True)