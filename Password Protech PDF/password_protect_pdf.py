from PyPDF2 import PdfWriter, PdfReader
import getpass
pdf_writer = PdfWriter()
pdf_reader = PdfReader("1.pdf")
for page_num in range(len(pdf_reader.pages)):
    pdf_writer.add_page(pdf_reader.pages[page_num])
password = "Password123"
pdf_writer.encrypt(user_password=password)
with open('converted.pdf', 'wb') as f:
    pdf_writer.write(f)
