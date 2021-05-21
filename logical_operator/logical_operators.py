# NOTE: haven't segregated operator based on binary/urinary as there is 3rd undefined category as well i.e,
# for operator like b/w, which takes 3 operands

import operator
from abc import ABC, abstractmethod

from exceptions import TotalOperandException, IllegalOperandsException
from utils import SingletonMixin


class LogicalOperator(ABC):
    """
    Abstract class for all operator
    """
    __total_operands: int
    __symbol: str
    __precedence: int

    @abstractmethod
    def _operate(self, operands: []):
        raise NotImplementedError()

    def validate(self, operands: []):
        # Placeholder for custom validation by each operator
        # May raise IllegalOperandsException()
        pass

    def operate(self, operands: []):
        if len(operands) != self.total_operands:
            raise TotalOperandException(self)
        try:
            self.validate(operands)
            return self._operate(operands)
        except TypeError:
            raise IllegalOperandsException(self)

    @property
    def total_operands(self):
        return self.__total_operands

    @property
    def symbol(self):
        return self.__symbol

    @property
    def precedence(self):
        return self.__precedence

    def __repr__(self):
        return str(self.symbol)


class GreaterThan(SingletonMixin, LogicalOperator):
    def __init__(self):
        self.__precedence = 4
        self.__symbol = '>'
        self.__total_operands = 2

    def _operate(self, operands):
        return operator.gt(operands[0], operands[1])


class GreaterThanEqualTo(SingletonMixin, LogicalOperator):
    def __init__(self):
        self.__precedence = 4
        self.__symbol = '>='
        self.__total_operands = 2

    def _operate(self, operands):
        return operator.ge(operands[0], operands[1])


class LessThan(SingletonMixin, LogicalOperator):
    def __init__(self):
        self.__precedence = 4
        self.__symbol = '<'
        self.__total_operands = 2

    def _operate(self, operands):
        return operator.lt(operands[0], operands[1])


class LessThanEqualTo(SingletonMixin, LogicalOperator):
    def __init__(self):
        self.__precedence = 4
        self.__symbol = '<='
        self.__total_operands = 2

    def _operate(self, operands):
        return operator.le(operands[0], operands[1])


class ExactlyEqualTo(SingletonMixin, LogicalOperator):
    def __init__(self):
        self.__precedence = 4
        self.__symbol = '=='
        self.__total_operands = 2

    def _operate(self, operands):
        return operator.eq(operands[0], operands[1])


class NotEqualTo(SingletonMixin, LogicalOperator):
    def __init__(self):
        self.__precedence = 4
        self.__symbol = '!='
        self.__total_operands = 2

    def _operate(self, operands):
        return operator.ne(operands[0], operands[1])


class AllOf(SingletonMixin, LogicalOperator):
    def __init__(self):
        self.__precedence = 5
        self.__symbol = 'ALLOFF'
        self.__total_operands = 3

    def _operate(self, operands):
        return operands[0] == operands[1] == operands[2]


class Between(SingletonMixin, LogicalOperator):
    def __init__(self):
        self.__precedence = 5
        self.__symbol = 'BETWEEN'
        self.__total_operands = 3

    def _operate(self, operands):
        return operands[1] <= operands[0] <= operands[2]


class NoneOf(SingletonMixin, LogicalOperator):
    def __init__(self):
        self.__precedence = 5
        self.__symbol = 'BETWEEN'
        self.__total_operands = 3

    def _operate(self, operands):
        return operands[1] != operands[0] and operands[0] != operands[2]


class Or(SingletonMixin, LogicalOperator):
    def __init__(self):
        self.__precedence = 1
        self.__symbol = 'OR'
        self.__total_operands = 2

    def validate(self, operands: []):
        if not all(map(lambda operand: isinstance(operand, bool), operands)):
            raise IllegalOperandsException("all operands are not of type boolean for operator: {}".format(self))

    def _operate(self, operands):
        return operands[0] or operands[0]


class And(SingletonMixin, LogicalOperator):
    def __init__(self):
        self.__precedence = 2
        self.__symbol = 'AND'
        self.__total_operands = 2

    def validate(self, operands: []):
        if not all(map(lambda operand: isinstance(operand, bool), operands)):
            raise IllegalOperandsException("all operands are not of type boolean for operator: {}".format(self))

    def _operate(self, operands):
        return operands[0] and operands[0]


class Not(SingletonMixin, LogicalOperator):
    def __init__(self):
        self.__precedence = 3
        self.__symbol = 'NOT'
        self.__total_operands = 1

    def validate(self, operands: []):
        if not all(map(lambda operand: isinstance(operand, bool), operands)):
            raise IllegalOperandsException("all operands are not of type boolean for operator: {}".format(self))

    def _operate(self, operands):
        return not operands[0]
