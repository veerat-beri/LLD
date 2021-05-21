import sys
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

    def create_user(self):
        pass
