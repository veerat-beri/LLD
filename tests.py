import unittest
from api import ApiInterface


class UserGatewayEntryTest(unittest.TestCase):
    def setUp(self) -> None:
        self.api_interface = ApiInterface()
        self.user_data = {
            'age': 24,
            'gender': 'female',
            'past_order_amount': 9000,
        }

    def test_denied_user(self):
        user = self.api_interface.create_user(**self.user_data)
        validation_expression = '( age > 25 and gender == male ) or past_order_amount > 10000'

        print('Created User: ', user)
        print('input validation expression: ', validation_expression)

        user_authorized = bool(self.api_interface.is_user_allowed(user, validation_expression))
        print("user authorised ?: ", user_authorized)
        self.assertEqual(user_authorized, False)
        print("\n\n\n")

    def test_allowed_user_1(self):
        user_data = {**self.user_data, **{"age": 25, "gender": 'male'}}
        user = self.api_interface.create_user(**user_data)
        validation_expression = '( age >= 25 and gender == male ) or past_order_amount > 10000'

        print('Created User: ', user)
        print('input validation expression: ', validation_expression)

        user_authorized = bool(self.api_interface.is_user_allowed(user, validation_expression))
        print("user authorised ?: ", user_authorized)
        self.assertEqual(user_authorized, True)
        print("\n\n\n")

    def test_allowed_user_2(self):
        user_data = {**self.user_data, **{'past_order_amount': 11000}}
        user = self.api_interface.create_user(**user_data)
        validation_expression = '( age >= 25 and gender == male ) or past_order_amount > 10000'

        print('Created User: ', user)
        print('input validation expression: ', validation_expression)

        user_authorized = bool(self.api_interface.is_user_allowed(user, validation_expression))
        print("user authorised ?: ", user_authorized)
        self.assertEqual(user_authorized, True)
        print("\n\n\n")


if __name__ == '__main__':
    unittest.main()
