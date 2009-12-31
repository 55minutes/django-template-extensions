"""
Some simple math filters.
"""
from django.template import Library

register = Library()


def multiply(value, arg):
    """Multiplies the arg and the value"""
    return int(value) * int(arg)
multiply.is_safe = False
multiply = register.filter('multiply', multiply)


def subtract(value, arg):
    """Subtracts the arg from the value"""
    return int(value) - int(arg)
subtract.is_safe = False
subtract = register.filter('subtract', subtract)


def divide(value, arg):
    """Divides the value by the arg"""
    return int(value) / int(arg)
divide.is_safe = False
divide = register.filter('divide', divide)
