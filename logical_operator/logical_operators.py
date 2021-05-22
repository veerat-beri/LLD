# NOTE: haven't segregated operator based on binary/urinary as there is 3rd undefined category as well i.e,
# for operator like b/w, which takes 3 operands
import json
import operator
from abc import ABC, abstractmethod, ABCMeta

from exceptions import TotalOperandException, IllegalOperandsException
from utils import SingletonMixin


class LogicalOperator(metaclass=ABCMeta):
    """
    Abstract class for all operator
    """
    _total_operands: int
    _symbol: str
    _precedence: int

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
        except (TypeError, ValueError):
            raise IllegalOperandsException(self, operands)

    @property
    def total_operands(self):
        return self._total_operands

    @property
    def symbol(self):
        return self._symbol

    @property
    def precedence(self):
        return self._precedence

    def __repr__(self):
        return str(self.symbol)


class GreaterThan(SingletonMixin, LogicalOperator):
    def __init__(self):
        self._precedence = 4
        self._symbol = '>'
        self._total_operands = 2

    def _operate(self, operands):
        operands[1] = type(operands[0])(operands[1])  # typecast second operand to same type of operand 1
        return operator.gt(operands[0], operands[1])


class GreaterThanEqualTo(SingletonMixin, LogicalOperator):
    def __init__(self):
        self._precedence = 4
        self._symbol = '>='
        self._total_operands = 2

    def _operate(self, operands):
        operands[1] = type(operands[0])(operands[1])  # typecast second operand to same type of operand 1
        return operator.ge(operands[0], operands[1])


class LessThan(SingletonMixin, LogicalOperator):
    def __init__(self):
        self._precedence = 4
        self._symbol = '<'
        self._total_operands = 2

    def _operate(self, operands):
        operands[1] = type(operands[0])(operands[1])  # typecast second operand to same type of operand 1
        return operator.lt(operands[0], operands[1])


class LessThanEqualTo(SingletonMixin, LogicalOperator):
    def __init__(self):
        self._precedence = 4
        self._symbol = '<='
        self._total_operands = 2

    def _operate(self, operands):
        operands[1] = type(operands[0])(operands[1])  # typecast second operand to same type of operand 1
        return operator.le(operands[0], operands[1])


class ExactlyEqualTo(SingletonMixin, LogicalOperator):
    def __init__(self):
        self._precedence = 4
        self._symbol = '=='
        self._total_operands = 2

    def _operate(self, operands):
        operands[1] = type(operands[0])(operands[1])  # typecast second operand to same type of operand 1
        return operator.eq(operands[0], operands[1])


class NotEqualTo(SingletonMixin, LogicalOperator):
    def __init__(self):
        self._precedence = 4
        self._symbol = '!='
        self._total_operands = 2

    def _operate(self, operands):
        operands[1] = type(operands[0])(operands[1])  # typecast second operand to same type of operand 1
        return operator.ne(operands[0], operands[1])


class AllOf(SingletonMixin, LogicalOperator):
    def __init__(self):
        self._precedence = 5
        self._symbol = 'ALLOFF'
        self._total_operands = 3

    def _operate(self, operands):
        operands[1] = type(operands[0])(operands[1])  # typecast second operand to same type of operand 1
        operands[2] = type(operands[0])(operands[2])  # typecast second operand to same type of operand 1
        return operands[0] == operands[1] == operands[2]


class Between(SingletonMixin, LogicalOperator):
    def __init__(self):
        self._precedence = 5
        self._symbol = 'BETWEEN'
        self._total_operands = 3

    def _operate(self, operands):
        operands[1] = type(operands[0])(operands[1])  # typecast second operand to same type of operand 1
        operands[2] = type(operands[0])(operands[2])  # typecast second operand to same type of operand 1
        return operands[1] <= operands[0] <= operands[2]


class NoneOf(SingletonMixin, LogicalOperator):
    def __init__(self):
        self._precedence = 5
        self._symbol = 'BETWEEN'
        self._total_operands = 3

    def _operate(self, operands):
        operands[1] = type(operands[0])(operands[1])  # typecast second operand to same type of operand 1
        operands[2] = type(operands[0])(operands[2])  # typecast second operand to same type of operand 1
        return operands[1] != operands[0] and operands[0] != operands[2]


class Or(SingletonMixin, LogicalOperator):
    def __init__(self):
        self._precedence = 1
        self._symbol = 'OR'
        self._total_operands = 2

    def validate(self, operands: []):
        if isinstance(operands[1], str):
            operands[1] = json.loads(operands[1])

        if not all(map(lambda operand: isinstance(operand, bool), operands)):
            raise IllegalOperandsException(message="all operands are not of type boolean for operator: {}".format(self))

    def _operate(self, operands):
        return operands[0] or operands[1]


class And(SingletonMixin, LogicalOperator):
    def __init__(self):
        self._precedence = 2
        self._symbol = 'AND'
        self._total_operands = 2

    def validate(self, operands: []):
        if isinstance(operands[1], str):
            operands[1] = json.loads(operands[1])

        if not all(map(lambda operand: isinstance(operand, bool), operands)):
            raise IllegalOperandsException(message="all operands are not of type boolean for operator: {}".format(self))

    def _operate(self, operands):
        return operands[0] and operands[1]


class Not(SingletonMixin, LogicalOperator):
    def __init__(self):
        self._precedence = 3
        self._symbol = 'NOT'
        self._total_operands = 1

    def validate(self, operands: []):
        if isinstance(operands[1], str):
            operands[0] = json.loads(operands[0])

        if not all(map(lambda operand: isinstance(operand, bool), operands)):
            raise IllegalOperandsException(message="all operands are not of type boolean for operator: {}".format(self))

    def _operate(self, operands):
        return not operands[0]
