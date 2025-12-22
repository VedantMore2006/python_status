import json

try:
    with open('config.json', 'r') as f:
        config = json.load(f)
except FileNotFoundError:
    print("The file not found or it seems to be missing")
    config = {}
except json.JSONDecodeError:   
    print("Config is corrupted")
    config = {}