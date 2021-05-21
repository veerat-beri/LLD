# from abc import ABC
# from typing import List
#
# from exceptions import ExecutionOrderException, InvalidExpressionException
# from serializer import Serializer
#
#
# class ExpressionParser(ABC):
#     """
#     Expression Parser Interface
#     """
#     def validate(self, *args, **kwargs):
#         raise NotImplementedError()
#
#     def get_parsed_expression(self, *args):
#         raise NotImplementedError()
#
#
# class InfixUserExpressionParser(ExpressionParser):
#     def __init__(self, expression_str: str, serializer: Serializer):
#         self.expression = expression_str
#         self.serializer = serializer
#         self.__is_valid = False
#         self.__validation_ran = False
#         self.__parsed_expression = []
#
#     def validate(self, *args, **kwargs):
#         """
#
#         :param args:
#         :param kwargs:
#         :return:
#         sample output:
#         [
#             {
#                 "age": {
#                     "operator": ">"
#                     "value": 25,
#                 }
#                 "gender": {
#                     "operator": "=="
#                     "value": "male",
#                 }
#             },
#             {
#                 "past_order_amount": {
#                     "operator": ">"
#                     "value": 10000,
#                 }
#             }
#         ]
#
#         """
#         for char in self.expression:
#             pass
#
#     def get_parsed_expression(self, *args) -> List[dict]:
#         if not self.is_valid:
#             raise InvalidExpressionException("Expression is not valid")
#         return self.__parsed_expression
#
#     @property
#     def is_valid(self):
#         if not self.__validation_ran:
#             raise ExecutionOrderException("Run validate method before expression correctness")
#         return self.__is_valid
