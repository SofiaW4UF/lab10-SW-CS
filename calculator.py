"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math

def square_root(a):
    if a < 0:
        raise ValueError
    return a ** 0.5

def hypotenuse(a, b):
    math.hypot(a, b)

def add(a, b): 
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    else:
        return b / a
def log(a, b):
    if b <= 0:
        raise ValueError
    else:
        return math.log(b, a)
def exp(a, b):
    return a ** b
