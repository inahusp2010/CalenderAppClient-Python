import json
from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass
class Employee:
    name: str
    email: str
    officeId: int
    dob: Optional[date]  # Optional in case dob can be None

    def object_to_json(self):
        return json.dumps(self.__dict__)

    def json_to_object(cls, json_str):
        json_data = json.loads(json_str)
        return cls(**json_data)
