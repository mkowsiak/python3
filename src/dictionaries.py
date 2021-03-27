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

d = {}                                      # empty dictionary
d = dict()                                  # empty dictionady via dictionary literal

d = {                                       # dictionary with initial values
    'key1' : 'val1',
    'key2' : 'val2'
}

d = dict(key1='val1', key2='val2')          # as above, this time, with dictionary literal

d['key1'] = 'val1'                          # assigning value to key
d['key2'] = 'val2'

v = d['key1']                               # accessing values in dictionary
v = d['key2']

#            int      string                # you can mix types inside dictionary
#             ↓         ↓                   # but try not to do that ;)
d = dict(key1=1, key2='val1')

del d['key1']                               # remove element with given key

try:                                        # you can't remove something that doesn't exist
    del d['no']
except KeyError:                            # there will be an error
    print("No value no")

d['key1'] = 'val10'                         # you can replace value in dictionary
d['key1'] = 'val11'

# dictionary methods

for k in d.keys():
    print("{} - {}".format(k, d[k]))

keys = list(d.keys())                       # note that d.keys() returns <class 'dict_keys'>
                                            # we have to create list here, if we want to operate on the list

for k in d:                                 # another way of iterating over keys - Python assumes we
    print("{} - {}".format(k, d[k]))        # are looking for keys

for i, k in enumerate(d):                   # yet another way of iterating over keys - this time with index
    print("{} - {}".format(i, k))

values = list(d.values())                   # getting list of all values

t = list(d.items())                         # we are getting the list of tuples (k, v)
                                            # [('key2', 'val2'), ('key1', 'val11')]


b = 'key1' in d                             # check whether key is already defined in dictionary
b = 'key3' not in d

d.get('key1')                               # almost the same as indexing with ['key1']

d.get('key3')                               # will return None - no exception here

d.get('key3', 'alternative value')
#                   │
#                   │
#                   └─── in case there is no value, you can provide alternative value

try:                                        # you can't access something that doesn't exist
    d['key3']
except KeyError:                            # there will be an error
    print("No value no")

e = d
e['key1'] = 'val3'                          # alias 'e' points at the same objec as 'd'

f = d.copy()                                # now, we have a copy of 'd' inside 'f'
f['key1'] = 'val4'                          # 'd' will not be altered


# accumulator pattern

s = "abcdefabcdefabcdef"

acc = {}

for c in s:
    if c not in acc:                        # 'not in' can tell you whether element is already there
        acc[c] = 0
    acc[c] += 1



