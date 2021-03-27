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

# map allows to transform input list by applying function on each element

def fun(x):
    return x + x


a = [1, 2, 3, 4, 5]

b = map(fun, a)                                 # apply 'fun' on each element in the list

print(a)
print(list(b))                                  # we have to cast - map returns <class 'map'> object


#          ┌───── function that will be applied on elements of the collection
#          │             ┌── collection of elements
#          │             │
#          │             │
b = map(lambda x: x + x, a)                     # apply lambda expression on each element in the list
print(list(b))


# filtering

a = [1, 2, 3, 4, 5]


#             ┌───── function that will determine whether element of collection should be used
#             │                  ┌── collection of elements
#             │                  │
#             │                  │
b = filter(lambda x: x % 2 == 0, a)             # filter function takes only elements that give True while
                                                # filtering function is applied on them
print(a)
print(list(b))                                  # we have to cast to list as we get <class 'filter'> here


def fun(x):
    if x % 2 == 0:
        return True
    else:
        return False


b = filter(fun, a)

print(a)
print(list(b))


# list comprehensions - simplified syntax for map/filter
# [ <transformation expression> for <loop_var> in <sequence> if <filter expression> ]

a = [1, 2, 3, 4, 5]
b = [x * 2 for x in a]                          # multiply each element in the list by 2

print(a)
print(b)


def odd(x):
    return x % 2


a = [1, 2, 3, 4, 5]
b = [odd(x) for x in a]                         # check whether number is odd or even using function
c = map(lambda x: odd(x), a)                    # check whether number is odd or even using lambda expression

print(a)
print(b)                                        # note that 'b' is a list after list comprehension
print(list(c))                                  # after calling map, we have to cast to list


# map and filter using comprehension vs. map/filter

b = [x for x in a if x % 2 == 0]                # note additional 'if' at the end that determines whether we
#    ↓     │    └──────┼─────────┐              # want to keep the element or not
#   expr.  └──────┐    │         │
#                 ↓    ↓         ↓
c = filter(lambda x: x % 2 == 0, a)


b = [x * 2 for x in a]
#      │       │    └────┐
#      └───────┼────┐    │
#              ↓    ↓    ↓
c = map(lambda x: x * 2, a)


print(a)
print(b)
print(list(c))


# zip - zipping two sequences together

a = [1, 2, 3, 4]                                # we want to combine these two into on
b = [5, 6, 7, 8]                                # by adding elements together

c = []

for i, v in enumerate(a):                       # we can enumerate over one list
    c += [v + b[i]]                             # and add elements from both lists and append result
                                                # to yet another list

print(a)
print(b)
print(c)


c = [x + y for (x, y) in list(zip(a, b))]       # but we can also zip them

zip(a, b)                                       # zips two list and creates object of type: <class 'zip'>

print(c)

a = [1, 2, 3, 4, 5]                             # if lists are not the same length
b = [1, 4, 5, 6]                                # you will get subset of the length of shorter list

print(list(zip(a, b)))

# you can add condition as in other comprehensions - add numbers if both are even

c = [x + y for (x, y) in list(zip(a, b)) if x % 2 == 0 and y % 2 == 0]

print(c)



