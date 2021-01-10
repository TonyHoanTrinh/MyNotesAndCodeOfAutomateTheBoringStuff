#! /usr/bin/env python3

import PyPDF2
pdfFileObj = open('./Automate_online-materials/meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)
pageObj = pdfReader.getPage(0)
print(pageObj.extractText())
