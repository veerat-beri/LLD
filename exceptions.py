class TotalOperandException(Exception):
    def __init__(self, operator_repr, message=''):
        self.operator = operator_repr
        self.message = message or 'incorrect operands count for operator: {}'.format(self.operator)
        super().__init__(self.message)


class IllegalOperandsException(Exception):
    def __init__(self, operator_repr, message=''):
        self.operator = operator_repr
        self.message = message or 'illegal operands for operator: {}'.format(self.operator)
        super().__init__(self.message)


class InvalidOperatorException(Exception):
    def __init__(self, operator_repr, message=''):
        self.operator = operator_repr
        self.message = message or 'operator: {} is not valid'.format(self.operator)
        super().__init__(self.message)


class SetUserAttributeException(Exception):
    def __init__(self, attribute: str, message=''):
        self.attribute = attribute
        self.message = message or 'Illegal type/value for user-attribute: {}'.format(self.attribute)
        super().__init__(self.message)
