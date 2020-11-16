"""Custom wrapper for function with a string representation."""


class DefaultOperator:
    """Default operator is a wrapper to a mathematical function with a string form."""

    def __init__(self, function_to_apply, string_repr_of_function):
        self.function_to_apply = function_to_apply
        self.string_repr_of_function = string_repr_of_function

    def __call__(self, *args):
        return self.function_to_apply(*args)

    def __str__(self):
        return self.string_repr_of_function
