#! /usr/bin/env python3
import requests

res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
print(res.status_code == requests.codes.ok)
print(len(res.text))

print(res.text[:250])
# res.raise_for_status() can be used to check if the download was successful

res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))


