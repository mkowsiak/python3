# -*- coding: utf-8 -*-
# automatic packing into tuple

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

a = (1, 2, 3, 4)                            # ⤵
                                            # these two are the same thing
a = 1, 2, 3, 4                              # ⤴


# returning tuples

def a():                                    # it's possible to return multiple values via tuple
    return 1, 2                             # automatic packing will happen here


a = 1, 2, 3, 4                              # automatic unpacking from tuple

x, y, z, v = a


# unpacking tuples as function parameters

def f(a, b):
    return a, b


a = 1, 2

f(*a)                                       # unpack tuple into function's arguments
try:
    f(a)                                    # this will fail as we treat tuple as a parameter
except TypeError:
    print("You can't pass tuple to this function")


# unpacking tuples inside for loop

d = {"k1": "v1", "k2": "v2"}


#   ┌─ key
#   │  ┌─ value
#   │  │
for k, v in d.items():
    print("k: {}, v: {}".format(k, v))


#   ┌─ (key, value)
#   │                           ┌─ unpacking tuple
#   │                           │
for i in d.items():
    print("k: {}, v: {}".format(*i))


# replacing values with tuples

a = 1
b = 2
(b, a) = (a, b)                             # we can swap them like this
b, a = a, b                                 # or like this
[b, a] = [a, b]                             # or this way


print(a, b)


