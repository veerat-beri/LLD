from abc import ABC, abstractmethod
from builtins import NotImplementedError

from exceptions import NoAvailableLockerException
from managers import LockerManager
from models import Locker


class LockerFindStrategy(ABC):
    @abstractmethod
    def get_next_available_locker(self, all_available_lockers: [], **kwargs):
        raise NotImplementedError()


class DefaultLockerFindStrategy(LockerFindStrategy):
    def get_next_available_locker(self, all_available_lockers, **kwargs) -> Locker:
        if not all_available_lockers:
            raise NoAvailableLockerException("Not locker is available")
        return all_available_lockers[0]

