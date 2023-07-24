import json
from dataclasses import dataclass


@dataclass
class MeetingRoom:
    name: str
    capacity: str
    officeId: int

    def object_to_json(self):
        return json.dumps(self.__dict__)

    def json_to_object(cls, json_str):
        json_data = json.loads(json_str)
        return cls(**json_data)
