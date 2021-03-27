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

f = open('data/simple.csv', 'r')


s = f.read()                                # read whole file
print(s)


f.seek(0)                                   # I am pretty sure you have seen that somewhere else ;)
a = f.readline()                            # read just one line
print(a)


f.seek(0)
a = f.readlines()                           # note that readline and readlines read '\n' as part of string
print(a)
for _ in a:
    print(_.strip())


f.seek(0)
for _ in f:                                 # we can use iteration byt we can't use slices (e.g.: f[:2]
    print(_.strip())

f.close()

# writing to files

f = open('data/output_test', 'w')

for _ in range(10):
    print(_, file=f)                        # we can print to file
    f.write(str(_) + '\n')                  # we can write to file - here, we have to add '\n' explicitly

f.close()

# accessing files via context manager

with open('data/simple.csv', 'r') as f:
    for line in f:
        print(line.strip())                 # note that we don't do f.close(); it's done automatically
                                            # after we leave the 'with' section
#
#
#
with open('data/output_test', 'w') as f:
    for _ in range(10):
        print(_, file=f)
        f.write(str(_) + '\n')

                                            # we don't have to call: f.close() - it's already done
                                            # while leaving the context manager

