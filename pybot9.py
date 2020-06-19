from pybot_random import choice_command, dice_command
from pybot_weather import weather_command

import math

def sqrt_command(command):
    sqrt, number_str = command.split()
    x = int(number_str)
    sqrt_x = math.sqrt(x)
    response = "{}ノ平方根は{}です".format(x, sqrt_x)
    return response

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
    try:
        date = command.split()
        year = int(date[1])
        month = int(date[2])
        day = int(date[3])
        one_day = date(year, month, day)

        weekday_str = "月火水木金土日"
        weekday = weekday_str[one_day.weekday()]

        response = "{}は{}曜日です".format(one_day, weekday)
    except IndexError:
        response = "3つの値（年月日）を指定ください"
    except ValueError:
        response = "正しい日付を指定してください"
    return response

def len_command(command):
    cmd, text = command.split()
    length = len(text)
    response  = "コノ文字列ノ長さは{}文字デス".format(length)
    return response

def heisei_command(command):
    heisei, year_str = command.split()
    if year_str.isdigit():
        year = int(year_str)
        if year >= 1989:
            heisei_year = year - 1988
            response = "西暦{}ハ、平成{}年デス".format(year, heisei_year)
        else:
            response = "西暦{}ハ、平成デハアリマセン".format(year)
    else:
            response = "数値を入れてください"
    return response

def eto_command(command):
    eto, year = command.split()
    eto_list = ["子", "うし", "とら", "うさぎ", "たつ", "巳", "午", "未", "さる", "とり", "いぬ", "いのしし"]
    eto_number = (int(year) + 8) % 12
    eto_name = eto_list[eto_number]
    response = "{}年生まれの干支は{}です".format(year, eto_name)
    return response

text_file = open('pybot.txt', encoding='utf-8')
raw_data = text_file.read()
text_file.close()
lines = raw_data.splitlines()

bot_dict = {}
for line in lines:
    word_list = line.split(',')
    key = word_list[0]
    response = word_list[1]
    bot_dict[key] = response

while True:
    command = input("pybot>")
    response = ''
    for message in bot_dict:
        if message in command:
            response = bot_dict[message]
            break

    if '平成' in command:
        response = heisei_command(command)
    if "長" in command:
        response = len_command(command)
    if "干支" in command:
        response = eto_command(command)
    if "選" in command:
        response = choice_command(command)
    if "さいころ" in command:
        response = dice_command()
    if "今日" in command:
        response = today_command()
    if "現在" in command:
        response = now_command()
    if "曜日" in command:
        response = weekday_command(command)
    if "平方" in command:
        response = sqrt_command(command)
    if "天気" in command:
        response = weather_command()

    if not response:
        response = "何を言っていますか？"
    print(response)

    if 'さようなら' in command:
        break
