from datetime import datetime, time, timedelta, date
import pytz
import json


def get_menu():
    IST = pytz.timezone('Asia/Kolkata')
    file = open("mess.json")
    mess_js = json.load(file)
    today = datetime.now(IST).replace(microsecond=0).date()

    trigger_time = [
        datetime.combine(today, time(6, 30, 0)),
        datetime.combine(today, time(11, 30, 0)),
        datetime.combine(today, time(16, 15, 0)),
        datetime.combine(today, time(18, 30, 0))
    ]
    reference_date = date(2021, 8, 22)
    reference_Id = 1

    check_first_date = str(today - reference_date)

    if (check_first_date[1] == ':'):
        new_Id = reference_Id
    else:
        days = (str(today - reference_date).split(' ')[0])
        new_Id = reference_Id + (int(days) % 28) * 4

    now_tz = datetime.now(IST).replace(microsecond=0)
    now = now_tz.replace(tzinfo=None)
    incr = 0

    for i in trigger_time:
        temp_date = (i - now)
        temp_date_str = str(temp_date)
        if (temp_date_str[0] != "-"):
            if ((temp_date_str[0] == '0') and (int(temp_date_str[2:4]) <= 10)):
                for menu_js in mess_js:
                    if (int(menu_js['Id']) == (new_Id + incr)):
                        return menu_js
        incr += 1

    return -1
