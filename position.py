import pdfplumber
from pdfminer.high_level import extract_pages
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from pdfminer.layout import LTTextBoxHorizontal, LTRect, LTTextBox, LTFigure, LTLayoutContainer, LTPage
from pdf2image import convert_from_path
from pathlib import Path

import fitz
file_path = "./pdf_files/jobi-1.pdf"
doc = fitz.open(file_path)
page = doc[0]
height = page.rect.height
width = page.rect.width
print(width)
print(height)
ratio = height/width
print(ratio)
new_height = 600 * ratio
# doc.close()
images = convert_from_path(
    file_path,
    output_folder='./images/',
    fmt='JPEG',
    size=(600,new_height)
    )


def pdf_converter():
        with pdfplumber.open('./jobi.pdf') as pdf:
            total_pages = len(pdf.pages)
            fulltext = ''
            for page in range(total_pages):
                page = pdf.pages[page]
                if page.extract_text() is not None:
                    fulltext += page.extract_text()
        return fulltext.split()


def get_boxes(path_to_file):
        document = open(path_to_file, 'rb')
        rsrcmgr = PDFResourceManager()
        laparams = LAParams()
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        page_number = 1
        cc = 1
        result = {}
        for page in PDFPage.get_pages(document):
            interpreter.process_page(page)
            layout = device.get_result()   
            for element in layout:
                if isinstance(element, LTTextBoxHorizontal):
                    # isinstance(element, LTRect) or
                    result[cc] = {
                        "x0": round(element.x0) + 3,
                        "y0": round(new_height - element.y0) - 11,
                        "x1": round(element.x1) + 3,
                        "y1": round(new_height - element.y1) - 11,
                        "page_number": page_number,
                    }
                    # result[cc] = {
                    #     "x0": round(element.x0),
                    #     "y0": round(element.y0),
                    #     "x1": round(element.x1),
                    #     "y1": round(element.y1),
                    #     "page_number": page_number,
                    # }
                    # print(dir(element))
                    print(result)
                    print(element.get_text())
                    # print('analyze',element.analyze)
                    # print(element)
                    cc += 1
                    result.clear()
            page_number += 1
        document.close()
        return result
{
"x0": 207,
"y0": 254,
"x1": 329,
"y1": 264,
},

target_box = {
'x0': 32.000,
'y0': 279.449,
'x1': 64.549,
'y1': 289.449,
'page_number': 1,
'name':'email'
}
target_box_2 = {
'x0': 207.000,
'y0': 504.438,
'x1': 402.830,
'y1': 515.438,
'page_number': 1,
'target':'jobs'
}
# <LTTextBoxHorizontal(20) 207.000, 504.438, 402.830, 515.438 'Sales Engineer, Engen Oil, Jacksonville\n'>
# Sales Engineer, Engen Oil, Jacksonville
# get_boxes()

def language_position_target(target_box):
    document = open('./right-blue-1.pdf', 'rb')
    rsrcmgr = PDFResourceManager()
    laparams = LAParams()
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    page_number = 1
    cc = 1
    result = {}
    # print(target_box['x0'])
    # print(type(target_box['x0']))
    # print(target_box['y0'])
    # print(target_box['x1'])
    # print(target_box['y1'])
    
    for page in PDFPage.get_pages(document):
        interpreter.process_page(page)
        layout = device.get_result()   
        for element in layout:
            # <LTTextBoxHorizontal(12) 32.000,279.449,64.549,289.449 'English\n'>
            if isinstance(element, LTTextBoxHorizontal):
                if round(element.x0) == round(target_box['x0']):                    
                    if round(element.y0) == round(target_box['y0']):
                        if round(element.x1) == round(target_box['x1']):
                            if round(element.y1) == round(target_box['y1']):
                                extracted_data = element.get_text()
    return extracted_data

# print(language_position_target(target_box))
get_boxes(file_path)
# pdf_to_image()