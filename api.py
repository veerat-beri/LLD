import sys
from expression.service import ExpressionService
from models import User


class ApiInterface:
    def __init__(self):
        self.service_inst = ExpressionService()

    def is_user_allowed(self, user: User, validation_expression):
        try:
            self.serializer_type.validate(user_data)
            expression_parser = self.parser_type(validation_expression, self.serializer_type())
            expression_parser.validate()
            valid_parsed_expression = expression_parser.get_parsed_expression()
            return self.service_inst.any_condition_match(user_data, valid_parsed_expression)

        except:
            print("Error: ", sys.exc_info()[0])
