# -*- coding: utf-8 -*-
# functions

# Copyright © 2021 Michal K. Owsiak. All rights reserved.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Any company and/or product names found in this book may be trademarks or
# registered trademarks of their owners.

def f():
    """ This comment will be used as docstring
        You can retrieve this information by calling f.__doc__ or help(f)"""
    print("Hello from f")


f()                                         # call 'f'

print(f.__doc__)
help(f)


def f(a, b):                                # you can pass parameters to function
    print(str(a) + str(b))                  # these are sometimes called: arguments, actual parameters
                                            # or parameter values


f(1, 2)


def f(a):
    return a                                # you have to use 'return' if you want to return value from function

print(f("a"))


def confusion(b):                           # "beauty" of Python based APIs at it's finest
    if b:                                   # Well, I am not quite sure what to return.
        return 1                            # Hm, maybe I will return int?
    else:
        return "a"                          # No, no, I've changed my mind. I like strings more than ints.


"""
                                            - Oh my God, your roommates were right, you really hate Python.
                                            - No, no, no, I don't. It's not hate, hate is a strong word.
                                              Truth be told, I have a slight preference for Java, but
                                              that's because, em, because I preffer precision.
"""

print(confusion(True))
print(confusion(False))

print(type(confusion(True)))
print(type(confusion(False)))

def confusing():                            # - Well, well, well. What do we have here?
    return 1
    return 2
    return 3


print(confusing())


# accessing global variables inside functions

x = 1                                       # global variable x
                                            #    │
                                            #    │
def f():                                    #    ↓
    return x + y                            #    x + y
                                            #        ↑
                                            #        │
y = 2                                       # global variable y


# shadowing global variables

def f():
    x = 1                                   # "I put a spell on you because you're mine
                                            #  I can't stand the things that you do
                                            #  No, no, no, I ain't lying"


x = 2


# using global variable

def f():
    global x                                # "I really really really really really really like you"
    x = 1                                   # try not to use global variables at all


x = 2


# mutable objects and functions

def f(d):
    d['key1'] = '- You, complete me.'


d = {"key1": "val1", "key2": "val2"}
f(d)                                        # d will change


d = {"key1": "val1", "key2": "val2"}
e = d
f(e)                                        # d will change


d = {"key1": "val1", "key2": "val2"}
e = list(d)
f(e)                                        # d will not change


d = {"key1": "val1", "key2": "val2"}
e = d.copy()
f(e)                                        # d will not change


# default values

del x                                       # let's make some cleaning before we proceed any further
del y


def a(x, y=1):                              # This one, works as expected
    y += 1
    return y


print(a(1))
print(a(2))


def a(x, y=[]):                             # Here, you have little surprise
    y += [1]                                # in this case, default value is mutable
    return y                                # and you can expect some side effects


print(a(1))                                 # can you see how 'y' is growing with each call to 'a'?
print(a(2))


# keywords parameters

def a(x=1, y=2):
    return x + y


a(3)                                        # x=3, y=2
a(3, 4)                                     # x=3, y=4
a(y=3)                                      # x=1, y=3

try:
    eval('a(y=3, 10)')
except SyntaxError:
    print("- If I make you feel second best; 'x', I'm sorry I was blind")


try:
    a(3, x=4)                               # don't even try to pass the same argument twice ;)
except TypeError:
    print(  "- I told you never to show your face here again, but here you are."
          + " Snooping around with this... What are you, a performer?"
          + " What's with the costume?")


# keywords can be useful while working with string.format

a, b, c = ("a", "b", "c")                   # unpack tuple into variables

print("{_a} {_b} {_c}".format(_a=a, _b=b, _c=c))
#       │    └────┼───────────┼─────┘     │
#       └─────────┼───────────┘           │
#                 └───────────────────────┘


value = 1


def a(x=value):                             # at the time of creation, value = 1
    return x                                # this is why default value of x = 1


value = 2                                   # even though we change value of the value here

a()


# lambdas

a = lambda x: x-1                           # define function using lambda

print(a(1))                                 # call it

print(lambda x: x-1)                        # take a closer look at lambda and it's type
print(type(lambda x: x-1))
print(a)
print(type(a))

print((lambda x: x-1)(1))                   # define function using lambda and call it

# you can make lambdas a little bit more complex

my_abs = lambda x: x if x >= 0 else -x
