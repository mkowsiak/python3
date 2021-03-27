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

# API  - Application Programming Interface
# REST - Representational State Transfer
# JSON - JavaScript Object Notation
# URL  - <scheme>://<host>:<port>/<path>
#
# It might be you need to install 'requests' and 'requests_cache' modules for this section
#
# pip3 install requests
# pip3 install requests_cache

# JSON
                                                # https://www.json.org
import json                                     # we need json module to work with JSON

json_string = """
{
    "key1": "va1",
    "key2": "val2"
}
"""

d = json.loads(json_string)

print(json_string)
print(d)
print(d['key1'])

#                       ┌───── keys inside JSON will be sorted alphabetically
#                       │
#                       │              ┌── defines indentation length inside serialized JSON
#                       │              │
#                       │              │
print(json.dumps(d, sort_keys=True, indent=2))  # note that format of output string is different
                                                # from one used as input for json.loads - here we have 2 spaces
import requests
import json

p = requests.get("https://api.datamuse.com/words?rel_rhy=Funny")
print(p.text)                                   # content of http response
print(p.url)                                    # gives you actual url that was used to make a call
                                                # this is useful for debugging as you can use this url
                                                # together with 'curl' application

print(p.json())                                 # shortcut for json.loads(page.text)
print(json.loads(p.text))                       # another way of enerating JSON object

print(p.status_code)                            # status code of your request - take a look below for full list
                                                # of HTTP status codes
                                                # https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
                                                # HTCPCP/1.0 - https://www.ietf.org/rfc/rfc2324.txt
print(p.headers)                                # header of the response - sometimes, you need to reach
                                                # inside header in order to get some info
json.loads(p.text)

# If you want to have more control over JSON data, you can do it with
# JSONDocker - https://github.com/mkowsiak/JSONDocker

p = requests.get("http://localhost:80/")        # if you want to use this code, make sure to run
print(p.text)                                   # JSONDocker. You can find it here
print(p.status_code)                            # https://github.com/mkowsiak/JSONDocker
                                                # you can customize JSON content
                                                # by changing index.php file

print(json.dumps(p.json(), sort_keys=True, indent=2))


# caching responses

import requests
import requests_cache                               # read more here: https://requests-cache.readthedocs.io/en/latest/

requests_cache.clear()
requests_cache.install_cache('memory', backend='memory')    # create new cache
for i in range(10):                                         # first call will take quite some time
    print("Call {}".format(i))                              # note how further calls are way faster
    requests.get("http://localhost:80/slow.php")            # get data - it will take 5 sec without cache

requests_cache.clear()

# APIs you might need
#
# https://affiliate.itunes.apple.com/resources/documentation/itunes-store-web-service-search-api/
# https://www.flickr.com/services/api/flickr.photos.search.html
# https://maps.googleapis.com/maps/api/geocode/json
# http://python-data.dr-chuck.net
# https://tastedive.com/read/api
# https://www.omdbapi.com
# http://www.datamuse.com/api/



