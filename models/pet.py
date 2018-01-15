import json


class Pet:
    def __init__(self, name="", breed="", age=0, weight=0.0, photo=""):
        self.name = name
        self.breed = breed
        self.age = age
        self.weight = weight
        self.photo = photo

    def to_json(self):
        return json.dumps(vars(self))
