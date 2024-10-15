import json

with open("gamedata.json", "r") as f:
    _gamedata = json.load(f)

chicken = _gamedata["chicken"]
inventory = _gamedata["inventory"]
items = {item["name"]: item for item in _gamedata["items"]}
shop = _gamedata["shop"]
attacks = _gamedata["attacks"]
enemies = _gamedata["enemies"]
