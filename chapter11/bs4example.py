#! /usr/bin/env python3

import requests, bs4
res = requests.get('http://nostarch.com')
res.raise_for_status()

noStarchSoup = bs4.BeautifulSoup(res.text, features = 'lxml')

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), features = 'lxml')

# Finding elements with select()
elems = exampleSoup.select('#author')
print(elems[0].getText())
print(str(elems[0]))
print(elems[0].attrs)

pElems = exampleSoup.select('p')
print(str(pElems[0]))
print(str(pElems[1]))
print(str(pElems[2]))
print(pElems[0].getText())
print(pElems[1].getText())
print(pElems[2].getText())

# Getting Data from an Element's attributes
spanElem = exampleSoup.select('span')[0]
print(str(spanElem))
print(spanElem.get('id'))
print(spanElem.get('some_nonexistent_addr'))
print(spanElem.attrs)

