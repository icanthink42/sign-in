import json

config_path = "config"

sign_in = {}
user_list = json.load(open(f"{config_path}/user_list.json", "r"))


def reset_day():
    pass
