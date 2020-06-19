import random

def choice_command(command):
    data = command.split()
    choiced = random.choice(data[1:])
    responce = "「{}」が選ばれました".format(choiced)
    return responce

def dice_command():
    num = random.randrange(1, 7)
    responce = "「{}」がでました".format(num)
    return responce
