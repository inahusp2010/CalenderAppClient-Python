import json


class Office:
    def __init__(self, name, location, totalRooms):
        self.name = name
        self.location = location
        self.totalRooms = totalRooms

    # def __str__(self):
    #     return f"Name: {self.name}, location: {self.location}, Total Roooms: {self.total_rooms}"

    def object_to_json(self):
        return json.dumps(self.__dict__)

    def json_to_object(cls, json_str):
        json_data = json.loads(json_str)
        return cls(**json_data)
