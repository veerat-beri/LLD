from typing import List

from logical_operator.factory import OperatorFactory
from utils import get_closing_opening_parenthesis_map


class ExpressionService:
    closing_opening_parenthesis_map = get_closing_opening_parenthesis_map()
    opening_parenthesis = set(closing_opening_parenthesis_map.values())

    def __init__(self):
        self.operator_factory = OperatorFactory()

    def is_operator(self, logical_operator):
        return self.operator_factory.get_operator(logical_operator) is not None

    def evaluate_postfix_expression(self, user_context: {}, postfix_expression: str):
        stack = []
        print("postfix_expression: ", postfix_expression)

        for element in postfix_expression.strip().split():
            # print(stack, element)
            if self.is_operator(element):
                logical_operator = self.operator_factory.get_operator(element)
                operands_list = [stack.pop() for _ in range(logical_operator.total_operands)]
                stack.append(logical_operator.operate(operands_list[::-1]))
                continue

            possible_attribute_val = user_context.get(element)
            if possible_attribute_val:
                stack.append(possible_attribute_val)
            else:
                stack.append(element)

        return stack.pop()

    def infix_to_postfix(self, expression: str):
        postfix_expr_str = ''
        operator_stack: List[str] = []
        delimiter = ' '

        for element in expression.strip().split():
            if self.is_operator(element):
                while operator_stack and (operator_stack[-1] not in self.opening_parenthesis) and \
                        self.operator_factory.get_operator(element).precedence <= self.operator_factory.get_operator(operator_stack[-1]).precedence:
                    postfix_expr_str += operator_stack.pop() + delimiter

                operator_stack.append(element)

            elif element in self.opening_parenthesis:
                operator_stack.append(element)

            elif element in self.closing_opening_parenthesis_map:
                corresponding_opening_parenthesis = self.closing_opening_parenthesis_map[element]
                while operator_stack and operator_stack[-1] != corresponding_opening_parenthesis:
                    postfix_expr_str += operator_stack.pop() + delimiter

                operator_stack.pop()  # pop opening bracket

            else:
                postfix_expr_str += element + delimiter

        while operator_stack:
            postfix_expr_str += operator_stack.pop() + delimiter

        return postfix_expr_str

    def evaluate_infix_expression(self, infix_expression, user_context):
        return self.evaluate_postfix_expression(user_context, self.infix_to_postfix(infix_expression))
