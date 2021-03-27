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

a = True

while a:
    a = False

a = 0

while True:                                 # "Break and Enter"
    if a == 1:
        break                               # go out from the loop
    a += 1
    if a == 1:
        continue                            # continue to next loop's step
    a += 1                                  # this line of code never runs

print(a)


while True:                                 # "Break and Enter"
    if a == 1:
        b = 0
        while True:                         # break terminates most inner loop
            break
    a += 1
    if a == 0:
        continue                            # continue to next loop's step
    elif a == 2:
        break                               # this break will jump out of outer while loop
    a += 1                                  # this line of code never runs


print(a)
