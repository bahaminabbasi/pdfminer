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

file_path = "./pdf_files/jobi-1.pdf"


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
                if isinstance(element, LTLayoutContainer):
                    # isinstance(element, LTRect) or
                    # result[cc] = {
                    #     "x0": round(element.x0) + 3,
                    #     "y0": round(new_height - element.y0) - 11,
                    #     "x1": round(element.x1) + 3,
                    #     "y1": round(new_height - element.y1) - 11,
                    #     "page_number": page_number,
                    # }

                    print(element)
                    # print(dir(element))
                    cc += 1
                    result.clear()
            page_number += 1
        document.close()
        return result

get_boxes(file_path)