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
    def __init__(self, name, age, gender, salary, past_order_amount, is_affluent, location: Location):
        self.name = name
        self.age = age
        self.gender = gender
        self.salary = salary
        self.past_order_amount = past_order_amount
        self.is_affluent = is_affluent
        self.location = location

    def __repr__(self):
        return f'User(name={self.name}, age={self.age}, gender={self.gender}, salary={self.salary}, ' \
               f'past_order_amount={self.past_order_amount})'
