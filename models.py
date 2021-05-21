from enum import Enum


class Gender(Enum):
    MALE, FEMALE, UNKNOWN = "male", "female", "unknown"


class Location:
    def __init__(self, city, latitude, longitude):
        self.city = city
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return f'Location(city={self.city}, latitude={self.latitude}, longitude={self.longitude})'


class User:
    def __init__(self):
        self.name = ''
        self.age = 0
        self.gender = Gender.MALE
        self.salary = 0
        self.past_order_amount = 0
        self.is_affluent = False
        self.location: Location = None

    def __repr__(self):
        return f'User(name={self.name}, age={self.age}, gender={self.gender}, salary={self.salary})'
