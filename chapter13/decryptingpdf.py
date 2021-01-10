#! /usr/bin/env python3

import PyPDF2 
pdfReader = PyPDF2.PdfFileReader(open('./Automate_online-materials/encrypted.pdf', 'rb'))
print(pdfReader.isEncrypted)
pdfReader.decrypt('rosebud')
pageObj = pdfReader.getPage(0)
