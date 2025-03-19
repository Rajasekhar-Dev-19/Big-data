from docx import Document

# Load the document
doc = Document('C:\Users\sekha\OneDrive\Desktop\Test\example_doc.docx')

# Iterate through paragraphs and print them
for para in doc.paragraphs:
    print(para.text)

# If you want to separate by pages, you might need to identify page breaks manually,
# as 'python-docx' does not directly support page-level reading.