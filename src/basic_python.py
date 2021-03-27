# -*- coding: utf-8 -*-
#        ↑
# If you want to use non-ascii characters inside your code, you will need that

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


# - Okay. Store's open. What do you need? Besides a miracle...
# - Comments. Lots of comments.

# This is a comment

"""
This is also a comment, but sort of "fraudulent comment" - technically, this is a string
but it's not associated to a variable, so, it's inaccessible.
"""

'''
This is also a comment, the same as above.
'''

# Different ways of importing modules

import random                       # whole module
import random  as rnd               # module aliased by rnd
from random import randint          # just a few things from the module

# Different ways of accessing symbols inside code

a = random.random()                 # via module name
b = rnd.random()                    # via module aliased by rnd
c = randint(1,2)                    # exposed in your code, thanks to importing name using from

# Arithmetic's gotchas
# - A lotta the same shit we got here, they got there, but there they're a little different.

a = 1 / 2                           # this is float!
print(str(a) + " " + str(type(a)))

a = 1.0 / 2                         # this is float!
print(str(a) + " " + str(type(a)))

a = 1 // 2                          # this is int! with floor applied!
print(str(a) + " " + str(type(a)))

a = 1.0 // 2                        # this is float! with floor applied!
                                    # note that this is not a rounding !

print(str(a) + " " + str(type(a)))

a = a**a                            # exp operator

a = 1 + 2j                          # this is complex number - note that we denote
                                    # imaginary part with 'j' instead of 'i'


a = ( 1 )                           # this is int
a = ( 1, )                          # this is one element tuple
a = [ 1 ]                           # this is one element array
a = [ ]                             # this is empty array
a = ( )                             # this is empty tuple - doesn't make too much sens as it is immutable

a = [  0,  1,  2,  3,  4,  5,  6,  7]
#      ↑                           ↑
#   a[ 0]                       a[ 7]
#   a[-8]                       a[-1]

a = a[1:4]                          # range is always in form of [a,b) - where [ - inclusive, ) - exclusive

a[0] = 100                          # you can change elements of array

print(a)

a = (  0,  1,  2,  3,  4,  5,  6,  7)
#      ↑                           ↑
#   a[ 0]                       a[ 7]
#   a[-8]                       a[-1]

print(a[0])                         # you can access tuple's elements

try:
    a[0] = 2                        # but "you can't touch this"
except TypeError:
    print("Ups! You can't touch data inside tuple")


# tuples and arrays can mix the types!


#   int  string    array
#    ↓     ↓         ↓
a = [1, "hello!", [1, 2]]           # by convention, tables should contain elements of the same type
                                    # try not to mix the types - it's legal, but try to avoid mixing

a = (1, "hello!", [1, 2])           # it's little bit different with tuples. Here, by convention, you can mix the types
#    ↑     ↑         ↑
#   int  string    array

len(a)                              # length of an array/tuple/string (number of elements)


a = [1, 2] + [3, 4]                 # you can concatenate lists
a = [1, 2] * 4                      # you can replicate lists
a.append(5)                         # you can also append single element into list
a += [6]
a += [7, 8]                         # another way of appending

a += [5, 6]                         # These two are two different things - here we append to existing list
b = a + [5, 6]                      # here, we create another list that is a result of concatenation

print(a)                            # these two, will be different
print(b)

c = a                               # it's different with alias and +=
c += [5, 6]                         # take a look here

print(a)
print(c)


a = (1, 2) * 4                      # you can multiply tuple by scalar (it means it will be concatenated with itself)
print(a)


# Strings

a = "This is a string"
b = "This ia another string"
c = a + b                           # This is concatenation of the strings 

#     ┌───── inclusive
#     │  ┌── exclusive
#     │  │
#     │  │
a = a[0: 2]                         # this is a subset of a string

a = "This is a string"
len(a)                              # this is the length of a string

a = a.index("This")                 # Index of first occurrence of the string inside another string

# range - generating ranges

a = range(5)                        # This is <class 'range'>
a = list(range(5))                  # now, we have a list

del a                               # "- Once Zion is destroyed, there is no need for me to be here."

try:
    print(a)
except NameError:
    print("Ups. It looks like agent 'a' Smith is no longer here.")

# Basic loop with "for"
#              ┌────── inclusive
#              │  ┌─── exclusive
#              │  │
#              │  │
for _ in range(1, 3):
    print(_)                        # you can access loop's index via '_' (undescore)
                                    # this line must be empty to tell Python we are done with the loop

print(_)                            # surprize! we can still access loop's index via '_'
                                    # remember this one? for(int i=1; i<3; i++) - 'i' was available only inside the loop

for _ in range(3):                  # if you don't specify lower index of range, it will start from 0
    print(_)

for _ in range(1, 3, 2):            # you can also specify step. In this sample: start = 1, end = 3, step = 2
    print(_)

for _ in "Hello":                   # iterate over all characters in the string
    print(_)

for _ in ["H", "e", "l", "l", "o"]: # iterate over array of strings
    print(_)


# enumerate - provide elements of array along with their index value
# idx1 value1
# idx2 value2
# ...

for idx, value in enumerate(["H", "e", "l", "l", "o"]):
    print(idx, value)

#                              start enumeration from ─┐
#                                                      │
for idx, value in enumerate(["H", "e", "l", "l", "o"], 2):
    print(idx, value)

# Counting elements

a = "Hello"

a.count("l")

a = [1, 2, 1, 2, 1, 2]
a.count(1)


a = [[1, 2], [1, 2], [2, 3]]
a = [1, 2] in a                     # True

a = [[1, 2], [1, 2], [2, 3]]
a = [3, 4] in a                     # False

a = [[1, 2], [1, 2], [2, 3]]
a = [3, 4] not in a                 # True

a = [[1, 2], [1, 2], [2, 3]]
a.count([1, 2])

a = ((1, 2), (1, 2), (2, 3))
a.count((1, 2))

# String split

a = "Hello world!"
a = a.split()                       # we get array of strings
print(a)

a = "Hello world!"                  # you can split by character
a = a.split("o")

a = "Hello world!"                  # you can split by whole words
a = a.split("wo")

"/".join(["a", "b", "c"])           # -> a/b/c

"".join(["a", "b", "c"])            # -> abc

"---".join(["a", "b", "c"])         # -> a---b---c


# Booleans

print(True)
print(False)

x = 2
y = 3

a = x == y                          # x is equal to y
a = x != y                          # x is not equal to y
a = x > y                           # x is greater than y
a = x < y                           # x is less than y
a = x >= y                          # x is greater than or equal to y
a = x <= y                          # x is less than or equal to y

# logical operators                 # 'or', 'and', 'not'

a = (x == y) and True
a = (x == y) or True
a = not (x == y)

# Precedence of operators

#   level       category       operators

# 7 (high)	    exponent	   **
# 6	         multiplication	   *,/,//,%
# 5	            addition	   +,-
# 4	           relational	   ==,!=,<=,>=,>,<
# 	            logical	       not
# 2	            logical	       and
# 1 (low)	    logical	       or

# Execution flow

# if-else and if-elif-else

a = rnd.randint(1, 100)
if a % 2 == 0:
    print("even")
else:
    print("odd")


a = rnd.randint(1,2)
if a == 0:
    print("zero")
elif a == 1:
    print("one")
else:
    print("two")


# if-else has to have at least one line of code

if a==0:                                    # it's not possible to have something like this
    # you can't leave this one empty        # a = 0;
    a = True                                # if( a == 1 ) {
                                            # } else {
                                            #   a = 1;
                                            # }

if a == 0:                                  # if you want to leave empty body - in case it's required
    pass                                    # you can use 'pass'
else:
    a = True


# Mutability

a = [1, 2, 3, 4]                            # replace one element
a[0:1] = [5, 6]                             # replace range
a[1:2] = []                                 # elements at indexes 1 and 2 will be removed from the list
                                            # don't use slicing for deleting

a = [1, 2, 3, 4]
del a[0]                                    # use 'del'

a = [1, 2, 3, 4]
del a[0:]

a = [1, 2, 3, 4]
del a[0:2]


# Strings are not mutable

a = "Error"

try:
    a[0] = "A"                              # nope!
except TypeError:
    print("Ups! You can't change string")

# we have to create new string

a = "A" + a[1:]

# For the strings, Python will very often make an alias
# instead of new variable
# but this is not always true! It may happen two strings are actually two, different objects
# use == to compare strings' content
#
# operator 'is' checks whether two variables are pointing at the very same object

a = "a"
b = "a"

print(a is b)                               # these are the same thing
print(a == b)                               # and are equal

a = [1, 2]
b = [1, 2]

print(a is b)                               # these are not the same thing
print(a == b)                               # but are equal

b = a
print(a is b)

# cloning the list

a = [1, 2]                                  # cloning by slicing
b = a[:]


# adding to list - be careful here!

a = [1, 2]

a += [3, 4]                                 # this is adding to the very same list
a = a + [5, 6]                              # this is creating a copy of 'a' and adding to new list!


# operations on lists

a = []
a += [1]
a.append(2)                                 # append at the end


#        ┌──── index
#        │  ┌─ new value
a.insert(1, 3)                              # we don't overwrite the value, we are shifting elements to the right

a.count(1)                                  # count how many times element appears in the list

a.index(1)                                  # index of first occurrence of '1'

a.reverse()                                 # changes the order of the list

a.sort()

del a[1]                                    # delete element at index '1'
a.remove(1)                                 # remove element with value '1'

a.pop()                                     # remove last element from the list and return it

# note! append, sort, reverse return None

a = [1, 2]
a.append(3)                                 # add to existing list

a = a + [4]                                 # new array is created
a += [5]                                    # we append to existing list


# strings

s = """Born from a foreign mother, his blood of ancient heroes,
And his name will be forty and four."""

u = s.upper()
l = s.lower()

s.count("o")                                # count how many letters or sub-strings there are in the string
s.count("or")

s.strip()                                   # two side trim (removes all white spaces - tab/space/new line)


#          ┌──── what do you want to change
#          │      ┌─ new value
s.replace("o", ".oOo.")


a = "a"
b = "b"

abc = "{}{}c".format(a, b)

#       ┌──╭── you can specify the number of argument to be placed here
#       │  │
aac = "{0}{0}c".format(a)

a = "{{ {} }}".format("a")                  # you can use {{ and }} to escape { and }

