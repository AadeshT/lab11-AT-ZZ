
# https://github.com/AadeshT/lab11-AT-ZZ.git
# Partner 1: Aadesh
# Partner 2: Zelun
import math

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math

def logarithm(a,b):
    if a<= 0 or a == 1 or b <= 0:
        raise ValueError
    return math.log(a,b)

def exponent (a,b):
    return a ** b


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def log(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid logarithm")
    return math.log(b, a)

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Division by zero")
    return b / a

def exp(a, b):
    return a ** b
