from pybot_weather import weather_command
from pybot_wikipedia import wikipedia_command

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

def pybot(command):
    #command = input("pybot>")
    response = ''
    for message in bot_dict:
        if message in command:
            response = bot_dict[message]
            break
    if '平成' in command:
        heisei, year_str = command.split()
        year = int(year_str)
        if 2019 >= year >= 1989:
            heisei_year = year - 1988
            response = "西暦{}ハ、平成{}年デス".format(year, heisei_year)
        else:
            response = "西暦{}ハ、平成デハアリマセン".format(year)
    if '天気' in command:
        response = weather_command()
    if '辞典' in command:
        response = wikipedia_command(command)
    if not response:
        response = "何を言っていますか？"
    return response

    #if 'さようなら' in command:
    #    break
