from pdfminer.high_level import extract_pages
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from pdfminer.layout import LTTextBoxHorizontal, LTRect, LTTextBox, LTFigure, LTLayoutContainer, LTPage,LTChar


def get_font_size(element):
    error_count = 0
    font_size = []
    for text_line in element:
        try:
            for character in text_line:
                if isinstance(character, LTChar):
                    if round(character.size) not in font_size:
                        font_size.append(round(character.size))
        except:
            error_count += 1 
    return font_size

def get_font_name(element):
    error_count = 0
    font_list = []
    for text_line in element:
        try:
            for character in text_line:
                if isinstance(character, LTChar):
                    # cleaned_font_name = re.sub(r'^.*?\+', '', character.fontname)
                    if character.fontname not in font_list:
                        font_list.append(character.fontname)
        except:
            error_count += 1 
    return font_list

def sorted_matching_section(path_to_file, box):
        document = open(path_to_file, 'rb')
        rsrcmgr = PDFResourceManager()
        laparams = LAParams()
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        page_number = 1
        cc = 1
        element_counter = 1
        result = {}
        # end_of_sections = 
        for page in PDFPage.get_pages(document):
            interpreter.process_page(page)
            layout = device.get_result() 
            for element in layout:
                if isinstance(element, LTTextBoxHorizontal):
                    if abs((round(element.x1) - box['x1'])) <= 2:
                        if get_font_name(element) == box['font_name']:
                            if get_font_size(element) == box['font_sieze']:
                                result[element_counter] = element
                                element_counter += 1
                cc += 1
                # result.clear()
            page_number += 1
        document.close()
        return result


# box = {'x0': 517, 'y0': 598, 'x1': 563, 'y1': 611, 'page_number': 1, 'content': 'اﻃﻼﻋﺎتاﻃﻼﻋﺎت', 'font_name': ['QECAAA+IRANSans-Bold'], 'font_sieze': [13]}
box = {'x0': 517, 'y0': 598, 'x1': 563, 'y1': 611, 'page_number': 1, 'content': 'اﻃﻼﻋﺎت\nاﻃﻼﻋﺎت\n', 'font_name': ['QJCAAA+IRANSans-Bold'], 'font_sieze': [13]}


rb1 = {'x0': 331, 'y0': 709, 'x1': 385, 'y1': 723, 'page_number': 1, 'content': 'ﻦﻣ هرﺎﺑرد\n', 'font_name': ['AAAAAA+IRANYekanWeb-Medium'], 'font_sieze': [14]}


rb1_2= {'x0': 296, 'y0': 420, 'x1': 384, 'y1': 434, 'page_number': 1, 'content': 'ﯽﻨﻓ یﺎﻫ ترﺎﻬﻣ', 'font_name': ['AAAAAA+IRANYekanWeb-Medium'], 'font_sieze': [14]}


# print(box['content'])
file_path = "./pdf_files/right-blue-1.pdf"
results = sorted_matching_items(file_path, rb1)
print(results)
