from exceptions import SetUserAttributeException
from models import Gender, Location, User


# Used Builder pattern to build User object
class UserBuilder:
    name = ''
    age = 0
    gender = Gender.MALE
    salary = 0.0
    past_order_amount = 0
    is_affluent = False
    location: Location = None

    def set_name(self, name: str):
        if not isinstance(name, str):
            raise SetUserAttributeException('name')
        self.name = name
        return self

    def set_age(self, age):
        if not isinstance(age, int):
            raise SetUserAttributeException('age')
        self.age = age
        return self

    def set_gender(self, gender):
        if gender not in [member.value for member in Gender]:
            raise SetUserAttributeException('gender')
        self.gender = gender
        return self

    def set_salary(self, salary):
        if not isinstance(salary, (int, float, )):
            raise SetUserAttributeException('salary')
        self.salary = float(salary)
        return self

    def set_past_order_amount(self, amount):
        if not isinstance(amount, int):
            raise SetUserAttributeException('past_order_amount')
        self.past_order_amount = amount
        return self

    def set_is_affluent(self, is_affluent):
        if not isinstance(is_affluent, bool):
            raise SetUserAttributeException('is_affluent')
        self.is_affluent = is_affluent
        return self

    def set_location(self, city='', lat=0, long=0):
        if not isinstance(city, str):
            raise SetUserAttributeException('city')

        if not isinstance(lat, (int, float, )):
            raise SetUserAttributeException('latitude')

        if not isinstance(lat, (int, float, )):
            raise SetUserAttributeException('longitude')

        self.location = Location(city, float(lat), float(long))
        return self

    def build(self) -> User:
        return User(self.name, self.age, self.gender, self.salary, self.past_order_amount, self.is_affluent,
                    self.location)
