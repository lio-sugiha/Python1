def eto_command(command):
    eto, year = .split(command)
    eto_list = ["子", "うし", "とら", "うさぎ", "たつ", "巳", "午", "未", "さる", "とり", "いぬ", "いのしし"]
    eto_number = (int(year) + 8) % 12
    eto_name = eto_list[eto_number]
    response = "{}年生まれの干支は{}です".format(year, eto_name)
    return response
