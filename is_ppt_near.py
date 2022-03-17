from datetime import datetime
import pytz

def is_ppt_now():
  IST = pytz.timezone('Asia/Kolkata')
  today = datetime.now(IST).today().weekday()
  bad_days = [1, 3, 5]
  if(today in bad_days):
    return True
  else:
    return False
  