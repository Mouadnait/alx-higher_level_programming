#!/usr/bin/python3
"""
Fetches a website URI with urllib
"""
import urllib.request


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        body = response.read()
        utf8_content = body.decode('utf-8')
    print("""Body response:
    - type: {}
    - content: {}
    - utf8 content: {}""".format(
        type(body), body, utf8_content))
