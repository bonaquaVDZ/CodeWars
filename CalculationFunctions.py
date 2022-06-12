'''
This time we want to write calculations using functions and get the results. Let's have a look at some examples:

seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3

Requirements:

There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
Each calculation consist of exactly one operation and two numbers
The most outer function represents the left operand, the most inner function represents the right operand
Division should be integer division. For example, this should return 2, not 2.666666...:

eight(divided_by(three()))

'''

# Ex 1
def zero(f = None): return 0 if f is None else int(f(0))
def one(f = None): return 1 if f is None else int(f(1))
def two(f = None): return 2 if f is None else int(f(2))
def three(f = None): return 3 if f is None else int(f(3))
def four(f = None): return 4 if f is None else int(f(4))
def five(f = None): return 5 if f is None else int(f(5))
def six(f = None): return 6 if f is None else int(f(6))
def seven(f = None): return 7 if f is None else int(f(7))
def eight(f = None): return 8 if f is None else int(f(8))
def nine(f = None): return 9 if f is None else int(f(9))

def plus(y): return lambda x: x + y
def minus(y): return lambda x: x - y
def times(y): return lambda x: x * y
def divided_by(y): return lambda x: x / y

print(one(times(three())))


# Ex 2
id_ = lambda x: x
number = lambda x: lambda f=id_: f(x)
zero, one, two, three, four, five, six, seven, eight, nine = map(number, range(10))
plus = lambda x: lambda y: y + x
minus = lambda x: lambda y: y - x
times = lambda x: lambda y: y * x
divided_by = lambda x: lambda y: y / x

# Ex 3
from functools import partial

def number(operation=None, integer=None):
    if operation is not None:
        return operation(integer)
    return integer

zero = partial(number, integer=0)
one = partial(number, integer=1)
two = partial(number, integer=2)
three = partial(number, integer=3)
four = partial(number, integer=4)
five = partial(number, integer=5)
six = partial(number, integer=6)
seven = partial(number, integer=7)
eight = partial(number, integer=8)
nine = partial(number, integer=9)

def plus(right: int):
    return lambda left: left + right
    
def minus(right: int):
    return lambda left: left - right

def times(right: int):
    return lambda left: left * right

def divided_by(right):
    return lambda left: left // right