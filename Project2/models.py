import threading
import uuid
from datetime import datetime
from random import randint

from exceptions import LockerFullException


class Address:
    pass


class User:
    def __init__(self, name, email='', address=None):
        self.__name = name
        self.__email = email
        self.__address = address
        self.__is_admin = False

    @property
    def name(self):
        return self.__name

    @property
    def email(self):
        return self.__email

    @property
    def is_admin(self):
        return self.__is_admin


class Admin(User):
    def __init__(self, name, email='', address=None):
        self.__is_admin = True
        super().__init__(name, email, address)


class Package:
    def __init__(self, name, size: int = 0):
        self.__name = name
        self.__size = size

    @property
    def name(self):
        return self.__name

    def __repr__(self):
        return f"Package(name={self.name})"

# class Location:


class Locker:
    def __init__(self, name, location=None):
        self.__id = uuid.uuid4()
        self.__name = name
        self.__location = location
        self.__package = None

    @property
    def name(self):
        return self.__name

    @property
    def location(self):
        return self.__location

    @property
    def id(self):
        return self.__id

    def add_package(self, package):
        lock = threading.Lock()
        lock.acquire()

        if self.__package is not None:
            raise LockerFullException(f"Locker={self.id} is already full ")

        self.__package = package
        lock.release()

    def remove_package(self):
        print(f"Removing package from locker: ", self.name)
        self.__package = None

    @property
    def package(self):
        return self.__package

    def __repr__(self):
        return f"Locker(name={self.name}, package= {self.package})"


class OtpLockerDetail:
    def __init__(self, for_user: User, locker: Locker, otp: int):
        self.__for_user = for_user
        self.__locker = locker
        self.__otp = otp
        self.__created_at = datetime.today().date()

    @property
    def created_at(self):
        return self.__created_at

    @property
    def locker(self):
        return self.__locker





