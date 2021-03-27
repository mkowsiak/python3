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

import random

a = [random.randint(0, 100) for x in range(1, 11)]  # generate 10 random values
a = list(random.sample(range(0, 100), 10))          # alternatively, you can use sample

print(a)

print(sorted(a))                                    # this one create new list with sorted values

a.sort()                                            # sort the list - this one modifies original list
                                                    # sort method returns None
print(a)


# reversing stuff

a = [1, 2, 3, 4, 5]

b = sorted(a, reverse=True)

c = list(reversed(a))

print(a)
print(b)
print(c)


# key parameter for sorted

my_abs = lambda x: x if x >= 0 else -x          # you can define very simple lambda


def my_abs(x):                                  # or function with one parameter
    if x >= 0:
        return x
    else:
        return -x


a = [7, -5, -1, -2, 7, -7]
#                         ↖
#    │   │   │   │  │   │ we apply key function on sequence
#    ↓   ↓   ↓   ↓  ↓   ↓     ↑
#   [7,  5,  1,  2, 7,  7]    │
#                             │
b = sorted(a, key=my_abs) #   │                 # key function associates key 'attribute' with each element in the
#              └──────────────┘                 # collection. Elements inside collection are sorted using
                                                # key 'attribute'. It's like sorting 'b' array while we actually
                                                # sort elements in array 'a'.

print(a)
print(b)


# sorting dictionaries

a = ['a', 'b', 'b', 'a', 'd', 'd', 'd', 'd', 'b', 'c']
d = {}

# let's count letters in 'a'

for c in a:
    if c in d:
        d[c] += 1
    else:
        d[c] = 1

print(d)

k = sorted(d)
print(k)

# what if we want to sort based on the count number instead

k = sorted(d, key=lambda e: d[e])               # in this case, key function tells us that we want to sort
                                                # using values instead of keys

print(k)

# we can also sort the whole list thanks to the fact we can get items of the dictionary
# represented as tuples

k = sorted(d.items(), key=lambda x: d[x[0]])    # 'x', in this case is a tuple of form ('a', 1), etc.
print(k)

print(dict(k))                                  # after data are sorted, we can turn them into dictionary again

# breaking ties in the primary sort order with a secondary sort order

a = [('a', '2', '1'),                           # for tuples, sorting acts following way
     ('b', '2', '1'),                           # sort by first element
     ('c', '2', '1'),                           # if there are ties, sort by second element
     ('a', '1', '2'),                           # etc.
     ('b', '1', '2')]

b = sorted(a)
print(a)
print(b)

# we can pass tuples as key

a = ['a', 'aa', 'aaa', 'b', 'bb', 'bbb', 'bbbb']

b = sorted(a, key=lambda word: (len(word), word))
print(a)
print(b)

# if we have a numeric key, we can use "-value" as key
# to enforce reverse order

a = ['a', 'aa', 'aaa', 'b', 'bb', 'bbb', 'bbbb']

b = sorted(a, key=lambda word: (-len(word), word))
print(a)
print(b)

# always remember the 'bogosort' ;) - the slowest sorting algorithm ;)
