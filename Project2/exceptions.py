from builtins import Exception


class LockerFullException(Exception):
    pass


class NoAvailableLockerException(Exception):
    pass


class UnAuthorizedException(Exception):
    pass