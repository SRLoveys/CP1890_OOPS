from dataclasses import dataclass


@dataclass
class Person:
    first_name: str = ""
    last_name: str = ""
    email_address: str = ""

    def get_fullname(self):
        return f"{self.first_name} {self.last_name}"
