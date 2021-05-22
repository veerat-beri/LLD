import sys

from builders import UserBuilder
from expression.service import ExpressionService
from models import User
from serializers import UserSerializer


class ApiInterface:
    def __init__(self):
        self.service_inst = ExpressionService()

    def is_user_allowed(self, user: User, expression: str):
        try:
            user_context = UserSerializer(user).data
            return self.service_inst.evaluate_postfix_expression(user_context, expression)
        except:
            print("Error: ", sys.exc_info()[0])

    def create_user(self, **kwargs):
        user_builder = UserBuilder()
        if age := kwargs.get('age'):
            user_builder = user_builder.set_age(age)

        if name := kwargs.get('name'):
            user_builder = user_builder.set_name(name)

        if gender := kwargs.get('gender'):
            user_builder = user_builder.set_gender(gender)

        if salary := kwargs.get('salary'):
            user_builder = user_builder.set_salary(salary)

        if past_order_amount := kwargs.get('past_order_amount'):
            user_builder = user_builder.set_past_order_amount(past_order_amount)

        if is_affluent := kwargs.get('is_affluent'):
            user_builder = user_builder.set_is_affluent(is_affluent)

        if kwargs.get('city') or kwargs.get('latitude') or kwargs.get('longitude'):
            user_builder = user_builder.set_location(
                kwargs.get('city', ''), kwargs.get('latitude', 0), kwargs.get('longitude', 0))

        return user_builder.build()


