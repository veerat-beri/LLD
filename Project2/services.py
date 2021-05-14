from datetime import datetime
from random import randint

from exceptions import UnAuthorizedException
from managers import LockerManager
from models import User, Package, OtpLockerDetail


def generate_otp():
    return randint(1000, 9999)


class LockerServices:

    def __init__(self, locker_manager=LockerManager(), max_duration=3):
        self.max_duration = max_duration
        self.locker_manager = locker_manager

    def vacate_lockers(self, vacated_by: User):
        if not vacated_by.is_admin:
            raise UnAuthorizedException("user not authorised")

        print("Vacating all filled lockers are: ")

        for locker in self.locker_manager.get_all_full_lockers():
            if (datetime.today().date() - locker.created_at) >= self.max_duration:
                locker.remove_package()

    def view_filled_lockers(self, vacated_by: User):
        if not vacated_by.is_admin:
            raise UnAuthorizedException("user not authorised")

        print("All filled lockers are: ")
        for locker in self.locker_manager.get_all_full_lockers():
            if (datetime.today().date() - locker.created_at) >= self.max_duration:
                print(locker)