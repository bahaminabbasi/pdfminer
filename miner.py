from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.layout import LAParams
from pdfminer.converter import TextConverter
from io import StringIO
from pdfminer.pdfpage import PDFPage
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTTextBox
from pdf2image import convert_from_path


path_to_pdf = "./farsi.pdf"

# images = convert_from_path(path_to_pdf)


# for i in range(len(images)):

#       # Save pages as images in the pdf
#     images[i].save('page'+ str(i) +'.jpg', 'JPEG')

for page_layout in extract_pages(path_to_pdf):
    for element in page_layout:
        if isinstance(element, LTTextContainer):
            print(element)


print(extract_pages(path_to_pdf))
