# -*- coding: utf-8 -*-

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


# - What about your Python code?
# - Well, things are getting pretty serious right now. I mean, I develop classes for, like, two hours
#   everyday so I guess you could say things are gettin' pretty serious.

# The state of an object represents those things that the object knows about itself.
# The state is stored in instance variables.

# Objects also have collection of methods that they can perform.


class Simple:
    pass                                        # nothing interesting here


class Str:
    def __init__(self):
        self.value = "Initial value"            # define instance attribute

    def get_value(self):
        return self.value                       # access instance attribute


s = Str()                                       # create instance of class 'Str'
print(s.get_value())                            # call method on instance 's'

s = Str()                                       # create instance once again
s.value = "Other value"                         # this time, change the value of attribute
print(s.get_value())


class Attr:
    def __init__(self):
        self.attr = "Test"
              # ↑
              # │
a = Attr()    # │
print(a.attr) # │                               # we are looking for 'attr'
#     ↑   ││    │                               # 1 - check whether instance has 'attr' variable
#     ╰ 1 ╯╰ 2 ─╯                               # 2 - check whether class has 'attr' variable
                                                # if we can't find it either in instane or in class
                                                # exception is thrown

try:
    print(b.missing_parts)                      # we are trying to call missing method on instance 'b'
except NameError:
    print("'missing_parts' is missing in object 'b'")


# Creating Instances from Data

s = ['a', 'b', 'c']
i = [1, 2, 3]
b = [True, False, True]
f = [1.0, 2.0, 3.0]
c = [1+2j, 2+3j, 3+4j]                          # imaginary part is denoted with 'j'

zipped = list(zip(s, i, b, f, c))
print(zipped)


class SimpleTypes:
    def __init__(self, s, i, b, f, c):
        self.s = s
        self.i = i
        self.b = b
        self.f = f
        self.c = c

    def __str__(self):
        return '{}, {}, {}, {}, {}'.format(self.s, self.i, self.b, self.f, self.c)


#                              ╭ unpack tuple ─╮ list of tuples
#                              │               │      │
#                              │               ↓      ↓
simple_types = list(map(lambda x: SimpleTypes(*x), zipped))     # creating list of objects using map

for elem in list(simple_types):
    print(elem)



#                            ╭ unpack tuple ─╮
#                            │               │
#                            ↓      ╭────────╯
simple_types = [SimpleTypes(*x) for x in zipped]                # creating list of objects using comprehensions
#                                           ↑
#                                           │
#                                     list of tuples

for elem in list(simple_types):
    print(elem)


#                                 ╭------ tuple ----──╮
#                                 │                   │
#                                 ↓                   │
simple_types = [SimpleTypes(v, w, x, y, z) for (v, w, x, y, z) in zipped]                # creating list of objects using comprehensions
#                                                                    ↑
#                                                                    │
#                                                              list of tuples


def fun(st):
    print(st)


for elem in list(simple_types):
    fun(elem)


class Attr:
    def __init__(self, s):
        self.attr = s

    def __str__(self):
        return self.attr

    def build(self):
        return Attr("Created by Attr: " + str(self.attr))       # you can return objects created by methods
                                                                # of a class


a = Attr("Test")
b = a.build()
print("{} - {}".format(a, b))


# Sorting

class Attr:
    def __init__(self, s):
        self.attr = s

    def __str__(self):
        return self.attr

    def sort_key(self):                                 # this function will serve as sorting key
        return len(self.attr)                           # take a look inside sorting.py to check out how keys work


L = [Attr('ccc'), Attr('a'), Attr('b'), Attr('aa')]

for i in sorted(L, key=Attr.sort_key):                  # using key value pointing at function inside class
    print(i)


L = [Attr('ccc'), Attr('a'), Attr('b'), Attr('aa')]

for i in sorted(L, key=lambda x: x.sort_key()):         # using key value pointing at function of object
    print(i)


class Attr:
    def __init__(self, s):
        self.attr = s

    def __str__(self):
        return self.attr

    def __lt__(self, other):                            # using overridden method '__lt__'
        return len(self.attr) < len(other.attr)


L = [Attr('ccc'), Attr('a'), Attr('b'), Attr('aa')]

for i in sorted(L):                                     # note that we don't have to pass 'key' anymore
    print(i)


# Class variables

class Attr:

    class_att = "Hello from class attribute"

    def __init__(self, s):
        self.attr = s

    def __str__(self):
        return self.attr


a = Attr("1")
b = Attr("2")
print("{} - {}".format(a, a.class_att))
print("{} - {}".format(b, b.class_att))


a.class_att = "Another value"                   # note that class variable is something little bit different
print("{} - {}".format(a, a.class_att))         # from static field
print("{} - {}".format(b, b.class_att))


# inheritance
#       ╭───────────────────────────────────────────────────╮
#       │                                                   │
#       ↓                                               #   │
class Attr:                                             #   │
    def __init__(self, s):                              #   │
        self.attr = s                                   #   │
                                                        #   │
    def __str__(self):                                  #   │
        return "Attr value: {}".format(self.attr)       #   │
#                                                           │
#                                                           │
# parent class ────┬────────────────────────────────────────╯
#                  ↓
class AttrWithTag(Attr):
    def __init__(self, s, t):
        super(AttrWithTag, self).__init__(s)                    # call to super class using 'super'
        self.tag = t

    def __str__(self):
        return "Tag: {} - {}".format(self.tag, Attr.__str__(self))


class AttrWithLabel(Attr):
    def __init__(self, s, l):
        Attr.__init__(self, l)                                  # call to super class using call to __init__
        self.label = l

    def __str__(self):
        return "Label: {} - {}".format(self.label, Attr.__str__(self))


class AttrWithNote(Attr):
    def __init__(self, s, n):
        super().__init__(n)                                     # call to super class using 'super()'
        self.note = n

    def __str__(self):
        return "Note: {} - {}".format(self.note, Attr.__str__(self))


a = Attr('a')
t = AttrWithTag('a', 't')
l = AttrWithLabel('a', 'l')
n = AttrWithNote('a', 'n')
print(t)
print(l)
print(n)

# how attributes are resolved when inheritance is involved in the process
#
#            a.attr
#               │
#               ↓
#   is 'attr' inside instance 'a'?
#               │
#               ├─── yes - a.attr
#               ↓
#               no
#               |
#   is 'attr' inside class of instance 'a' ─────────────────╮
#               │                                           │
#               ├─── yes - get attribute from the class     │
#               ↓                              │            │
#               no                             ↓            ↑
#               |                             STOP          │
#      do I have a parent class?                            │
#               │                                           │
#               ├─── yes ───────── check parent class ──────╯
#               ↓
#               no
#               │
#               ↓
#              UPS!


# overriding methods

#           ╭────── 'method' is overridden in class B ──╮
#           ↑                                           │
class A:                                        #       │
    def method(self):                           #       │
        print('A')                              #       │
#                                                       │
#            ╭──────────────────────────────────────────╯
#            ↓
class B(A):                                     #
    def method(self):                           #
        print('B')

    def method_from_a(self):
        A.method(self)                          # we can access it by referring to parent's class directly
        super().method()                        # we can still call it by calling super()
        super(B, self).method()                 # we can call it using super and our own type


a = A()
b = B()

a.method()
b.method()
b.method_from_a()


class A:
    def __init__(self):
        self.att = 'a'


class B:
    def __init__(self):
        self.txt = 'bb'
        self.att = 'b'


#               ╭───────────────────────────────────────────────────╮
#               ↓                                                   │
class C(A, B):                                                  #   │
    def __init__(self):                                         #   │
        A.__init__(self)                                        #   │
        B.__init__(self)                                        #   │
                                                                #   │
    def __str__(self):                                          #   │
        return "att: {} txt: {}".format(self.att, self.txt)     #   │
#                                                                   │
#               ╭──── note the order of calls to parents ───────────╯
#               ↓
class D(A, B):
    def __init__(self):
        B.__init__(self)                            # 'att' and 'txt' will slightly differ in C and D
        A.__init__(self)                            # instances because we have different order of calls
                                                    # to parents' __init__ methods - be careful!
    def __str__(self):
        return "att: {} txt: {}".format(self.att, self.txt)


c = C()
print(c)                                            # take a look at value of att

d = D()
print(d)                                            # take a look at value of att here - have you noticed something?


# The diamond problem of multiple inheritance


class A:
    def a(self):                            # this method is inherited
        print('a')


class B(A):
    def a(self):                            # here
        print('b')


class C(A):
    def a(self):                            # and here
        print('c')


class D(B, C):                              # we don't define method 'a' inside 'D'
    pass                                    # which method will be called? A.a or B.a?


class E(C, B):                              # and what about E?
    pass


d = D()                                     # Python resolves naming conflicts based on inheritance order
d.a()                                       # from left to right
e = E()
e.a()

