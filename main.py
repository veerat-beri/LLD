from api import ApiInterface


def test_user_gateway():
    user_data = {
        'age': 24,
        'gender': 'female',
        'past_order_amount': 9000,
    }
    api_interface = ApiInterface()
    user = api_interface.create_user(**user_data)

    print('User: ', user)
    expression = '( age > 25 and gender == male ) or past_order_amount > 10000'
    print('is user allowed:', bool(api_interface.is_user_allowed(user, expression)))


if __name__ == '__main__':
    test_user_gateway()
