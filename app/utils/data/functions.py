def map_insertion_list(mapper, list):
  mapped_list = []
  for l in list:
    mapped_list.append(mapper(l))
  return mapped_list