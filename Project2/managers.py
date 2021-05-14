from models import Locker, Package


class PackageManager:
    pass


class LockerManager:
    lockers = []
    booked_locker_details = {}

    def add_locker(self, name, **kwargs):
        locker = Locker(name)
        LockerManager.lockers.append(locker)
        return locker

    # Helper Method
    def get_free_lockers(self):
        res = []
        for locker in LockerManager.lockers:
            if locker.package is None:
                res.append(locker)

        return res

    def add_package_to_locker(self, locker, package: Package):
        locker.add_package(package)

    def get_all_full_lockers(self):
        res = []
        for locker in self.locker_manager.lockers:
            if locker.package is not None:
                res.append(locker)
        return res

