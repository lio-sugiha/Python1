from datetime import date, datetime

def today_command():
    today = date.today()
    response = "今日の日付は{}です。".format(today)
    return response

def now_command():
    now = datetime.now()
    response = "現在の日時は{}です。".format(now)
    return response

def weekday_command(command):
    date = command.split()
    year = int(date[1])
    month = int(date[2])
    day = int(date[3])
    one_day = date(year, month, day)

    weekday_str = "月火水木金土日"
    weekday = weekday_str[one_day.weekday()]

    response = "{}は{}曜日です".format(one_day, weekday)
    return response
