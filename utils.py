from abc import ABC
from threading import Lock


class SingletonMixin(ABC):
    """
    Ensures Singleton design pattern in all concrete classes which inherit this abstract class
    """
    __singleton_instance = None
    __lock = Lock()

    def __new__(cls, *args, **kwargs):
        if cls.__singleton_instance is None:
            cls.__lock.acquire()
            if cls.__singleton_instance is None:
                cls.__singleton_instance = super().__new__(cls, *args, **kwargs)
            cls.__lock.release()
        return cls.__singleton_instance


def get_closing_opening_parenthesis_map():
    return {
        '}': '{',
        ']': '[',
        ')': '(',
        '>': '<',
    }
