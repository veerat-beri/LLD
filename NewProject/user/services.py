from os import name

from user.model import User

users = {}


def add_user(user_name):
    users[user_name] = User(name)

