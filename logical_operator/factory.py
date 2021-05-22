from typing import Dict

from exceptions import InvalidOperatorException
from logical_operator.logical_operators import GreaterThan, GreaterThanEqualTo, LessThan, LessThanEqualTo, ExactlyEqualTo, NotEqualTo, \
    AllOf, Between, NoneOf, LogicalOperator, Or, And, Not
from utils import SingletonMixin


class OperatorFactory(SingletonMixin):
    """
    Singleton class for storing and handling mapping of each logical_operator symbol to its actual logical_operator handler
    """
    __operator_map: Dict[str, LogicalOperator] = {}

    def __init__(self):
        if not self.__operator_map:
            self.__operator_map = {
                logical_operator.symbol: logical_operator for logical_operator in [
                    GreaterThan(), GreaterThanEqualTo(), LessThan(), LessThanEqualTo(), ExactlyEqualTo(),
                    NotEqualTo(), AllOf(), Between(), NoneOf(), Or(), And(), Not()]
            }
            print("Available operators: ", list(self.__operator_map.keys()), end='\n\n')

    @property
    def available_operators(self):
        return self.__operator_map

    def get_operator(self, operator_symbol: str) -> LogicalOperator:
        return self.available_operators.get(operator_symbol.upper())

    def get_operator_or_raise(self, operator_symbol: str) -> LogicalOperator:
        logical_operator = self.get_operator(operator_symbol)
        if not logical_operator:
            raise InvalidOperatorException(operator_symbol)
        return logical_operator
