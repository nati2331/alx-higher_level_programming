#!/usr/bin/python3
"""
takes in a URL
"""

import sys
import urllib.request
import urllib.error

if __name__ == "__main__":
    url = sys.argv[1]

    own_request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(own_request) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
