import os
import json

CONFIG_DIR = ".envsync"
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")


def save_config(data):

    if not os.path.exists(CONFIG_DIR):
        os.makedirs(CONFIG_DIR)

    with open(CONFIG_FILE, "w") as f:
        json.dump(data, f)


def load_config():

    if not os.path.exists(CONFIG_FILE):
        return None

    with open(CONFIG_FILE, "r") as f:
        return json.load(f)