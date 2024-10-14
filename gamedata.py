import json

with open("gamedata.json", "r") as f:
    _gamedata = json.load(f)

chicken = _gamedata["chicken"]
