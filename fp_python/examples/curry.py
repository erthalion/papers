class Curry(object):
    def __init__(self, function):
        self.function = function
        self.expected_arguments = function.func_code.co_argcount
        self.arguments = []

    def __call__(self, argument):
        self.arguments.append(argument)
        if len(self.arguments) == self.expected_arguments:
            return self.function(*self.arguments)
        else:
            return self
