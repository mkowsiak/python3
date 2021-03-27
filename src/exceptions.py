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

# - There is an error! What should we do?
# - null? throw? zero? maybe none? I have no idea. It's a technicolor yawn.

import sys                                      # for sys.exc_info
import traceback
import random

try:
    a = 1
    a = a/0                                     # try to do some nasty thing
except ZeroDivisionError as ex:                 # we can assign exception to variable
    print("a/0 gives: " + str(ex))              # and print the message


flag = [True, True]                             # this flag will tell us whether we have 'visited' both exception
while flag != [False, False]:                   # or not
    try:
        a = []
        b = 1
        rnd = random.randint(0, 1)              # heads or tails
        if rnd == 0:
            a = a[2]                            # try to access invalid index
        else:
            b = b/0                             # try to divide
    except ZeroDivisionError as ex:             # depending on error, we will end up here
        flag[0] = False
        print(ex)
    except IndexError as ex:                    # or here
        flag[1] = False
        print(ex)
    finally:                                    # this one is printed once we leave try/except block
        print("- Ups. I did it again.")         # you can do some cleaning here

print("Finally! The horror is over!")

try:
    a = 1
    a = a/0
except:                                         # you can leave type of exception empty, but you shouldn't
    t, v, bt = sys.exc_info()                   # unpack exception info
    traceback.print_tb(bt)                      # print back trace of exception
    print(v)                                    # print message
    traceback.print_exception(t, v, bt)


try:
    raise Exception('Ups! Somebody has thrown an exception!')
except Exception as ex:
    print(ex)


# if/else vs try/except

a = {'a': 1, 'b': 2}                            # a contains various keys

if 'c' in a:                                    # if we expect that element might be missing
    print(a['c'])                               # we should go with if/else
else:
    print("There is no key 'c'")

try:                                            # if we assume that 'c' is always inside 'a'. But it may
    print(a['c'])                               # happen due to error it is missing, we should go with
except:                                         # try/except
    print("There is no key 'c'")


# for the list of all built-in exceptions, take a look here
# https://docs.python.org/3/library/exceptions.html

#    The class hierarchy for built-in exceptions is:
#
#    BaseException
#    ├── Exception
#    │   ├── ArithmeticError
#    │   │   ├── FloatingPointError
#    │   │   ├── OverflowError
#    │   │   └── ZeroDivisionError
#    │   ├── AssertionError
#    │   ├── AttributeError
#    │   ├── BufferError
#    │   ├── EOFError
#    │   ├── ImportError
#    │   │   └── ModuleNotFoundError
#    │   ├── LookupError
#    │   │   ├── IndexError
#    │   │   └── KeyError
#    │   ├── MemoryError
#    │   ├── NameError
#    │   │   └── UnboundLocalError
#    │   ├── OSError
#    │   │   ├── BlockingIOError
#    │   │   ├── ChildProcessError
#    │   │   ├── ConnectionError
#    │   │   │   ├── BrokenPipeError
#    │   │   │   ├── ConnectionAbortedError
#    │   │   │   ├── ConnectionRefusedError
#    │   │   │   └── ConnectionResetError
#    │   │   ├── FileExistsError
#    │   │   ├── FileNotFoundError
#    │   │   ├── InterruptedError
#    │   │   ├── IsADirectoryError
#    │   │   ├── NotADirectoryError
#    │   │   ├── PermissionError
#    │   │   ├── ProcessLookupError
#    │   │   └── TimeoutError
#    │   ├── ReferenceError
#    │   ├── RuntimeError
#    │   │   ├── NotImplementedError
#    │   │   └── RecursionError
#    │   ├── StopAsyncIteration
#    │   ├── StopIteration
#    │   ├── SyntaxError
#    │   │   └── IndentationError
#    │   │       └── TabError
#    │   ├── SystemError
#    │   ├── TypeError
#    │   ├── ValueError
#    │   │   └── UnicodeError
#    │   │       ├── UnicodeDecodeError
#    │   │       ├── UnicodeEncodeError
#    │   │       └── UnicodeTranslateError
#    │   └── Warning
#    │       ├── BytesWarning
#    │       ├── DeprecationWarning
#    │       ├── FutureWarning
#    │       ├── ImportWarning
#    │       ├── PendingDeprecationWarning
#    │       ├── ResourceWarning
#    │       ├── RuntimeWarning
#    │       ├── SyntaxWarning
#    │       ├── UnicodeWarning
#    │       └── UserWarning
#    ├── GeneratorExit
#    ├── KeyboardInterrupt
#    └── SystemExit
