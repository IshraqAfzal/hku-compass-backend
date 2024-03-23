from datetime import datetime

def calculate_strm():
  strm = "4"
  current_date = datetime.now().date()
  year = current_date.year
  month = current_date.month
  if month < 7:
    strm += str(year - 1)[2:4] + '2'
  else:
    strm += str(year)[2:-1] + '1'
  return strm

def decode_strm(strm : str):
  year = "20" + strm[1:3] + "-" + str(int(strm[1:3]) + 1)
  semester = strm[-1]
  return [year, semester]