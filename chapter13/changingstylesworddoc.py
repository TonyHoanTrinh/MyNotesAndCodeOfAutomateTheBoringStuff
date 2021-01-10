doc = docx.Document('./Automate_online-materials/demo.docx')
print(doc.paragraphs[0].style)
doc.paragraphs[0].style = 'Normal'

doc.paragraphs[1].runs[0].style = 'QuoteChar'
doc.paragraphs[1].runs[1].underline = True
doc.paragraphs[1].runs[3].underline = True
doc.save('restyled.docx')


