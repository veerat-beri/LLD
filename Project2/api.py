from datetime import datetime

from exceptions import UnAuthorizedException
from managers import LockerManager
from models import Package, OtpLockerDetail, User
from services import generate_otp
from startegies import DefaultLockerFindStrategy


class API:
    locker_details = []
    MAX_DURATION = 3

    def __init__(self, locker_manager=LockerManager(), locker_find_strategy=DefaultLockerFindStrategy()):
        self.locker_manager = locker_manager
        self.locker_find_strategy = locker_find_strategy

    def create_locker(self, name):
        print("Adding Locker")
        return self.locker_manager.add_locker(name)

    def allocate_locker(self, for_user: User, package: Package):
        free_lockers = self.locker_manager.get_free_lockers()
        available_locker = self.locker_find_strategy.get_next_available_locker(free_lockers)
        self.locker_manager.add_package_to_locker(available_locker, package)
        otp = generate_otp()
        otp_locker_detail = OtpLockerDetail(for_user, available_locker, otp)
        API.locker_details.append(otp_locker_detail)
        return otp

    def unlock_locker(self, locker_details: OtpLockerDetail):
        locker_details.locker.remove_package()

    def vacate_lockers(self, vacated_by):
        pass

    def view_filled_lockers(self, vacated_by):
        pass











