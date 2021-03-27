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

a = [[1,2], [3, 4], [5, 6]]                     # nested loop

                                                #   ┌──→ [1, 2]
                                                # a[0]
                                                # a[1] → [3, 4]
                                                # a[2]
                                                #   └──→ [5, 6]

a = [{'a': 1, 'b': 2}, {'c': 4}, {'d': 4}]      # list of dictionaries


def f(x):                                       # we need few dummy functions
    return 1 + x                                # 'f'


def g(x):                                       # 'g'
    return "string" + str(x)


def h(x):                                       # and 'h'
    if x > 0:
        return True
    else:
        return False                            # it is really not that important what they do


a = [f, g, h, lambda x: x+2]                    # what's important is, that we can have list of functions as well

for fun in a:                                   # and we can iterate over it, and call each and every function
    print(fun(1))                               # that is on the list


# nested dictionaries

d = {                                           # indentation is a matter of the taste, I guess
    'a': {                                      # but you can read about best practices here
        'b': {                                  # https://www.python.org/dev/peps/pep-0008/
            'c': '- I am down here!'
        }
    }
}

value = d['a']['b']['c']
print(value)


# nested loops for accessing dictionaries

a = [{'a': 1, 'b': 2}, {'c': 4}, {'d': 4}]

for i in a:
    print(i)
    for p in i:
        print("  {} -> {}".format(p, i[p]))


# check whether nested element is iterable

a = [1, 2, {'a': 1, 'b': 2}, ['c', 4], {'d': 4}]    # don't mix the types in the list

for i in a:
    if type(i) is dict:                             # but, if you do, make sure to check what you are looking at
        for p in i:
            print("d:  {} -> {}".format(p, i[p]))
    elif type(i) is list:                           # and check with if/elif/else
        for p in i:
            print("l:  {}".format(p))
    else:
        print("v  {}".format(i))


# shallow copy vs. deep copy

a = [[1, 2], [3, 4]]                        # here, we have alias
b = a                                       # a → [[1, 2], [3, 4]]
                                            #       ↑
print("{} - {}".format(a,b))                # b ────┘
print(a is b)
print(a == b)


a = [[1, 2], [3, 4]]                        # here, we do copy, and we have
b = a[:]                                    # a → [[1, 2], [3, 4]]
                                            # b → [[1, 2], [3, 4]]

print("{} - {}".format(a,b))
print(a is b)
print(a == b)                               # however, be careful here!

a[0].append(3)                              # we add to firs list inside list 'a'

print(a)                                    # and both lists are affected!
print(b)                                    # this is because list 'b' is a shallow copy and inner lists point
                                            # point at the same objects

import copy                                 # we need copy package to perform deepcopy (unless your class provides
                                            # this method by it's own.

a = [[1, 2], [3, 4]]                        # here, we do deepcopy, and we have
b = copy.deepcopy(a)                        # a → [[1, 2], [3, 4]]
                                            # b → [[1, 2], [3, 4]]
                                            # where each inner list is also a copy

print("{} - {}".format(a,b))
print(a is b)
print(a == b)

a[0].append(3)                              # we add to firs list inside list 'a'

print(a)                                    # just a list is affected by adding new element
print(b)                                    # this is because list 'b' is a deep copy of 'a'
                                            # and inner objects point to different things

# looping over selected range of items

a = [[1, 2], [3, 4], [5, 6], [7, 8]]

for i in a:                                 # we are looping over all the elements
    print(i)

for i in a[:1]:                             # get just one element - first
    print(i)

for i in a[-1:]:                            # get just one element - last
    print(i)                                # don't do a[-1] - in this case you will iterate over elements of inner list

