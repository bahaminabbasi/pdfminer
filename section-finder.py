import pdfplumber
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTChar, LTText
from pdfminer.layout import LTTextBoxHorizontal






file_path = "./pdf_files/jobi-1.pdf"
page_number = 1
cc = 1
result = {}
font_list = []
single_font_dict = {}
font_detail = {}
error_count = 0

# section_box = {'x0': 528, 'y0': 541, 'x1': 563, 'y1': 554, 'page_number': 1, 'content': 'ﻣﻬﺎرت ﻣﻬﺎرت\n', 'font_name': ['QJCAAA+IRANSans-Bold'], 'font_sieze': [13], 'text_color': [[0.976470588, 0.650980392, 0.043137254]]}
# item_box = {'x0': 494, 'y0': 498, 'x1': 529, 'y1': 509, 'page_number': 1, 'content': 'HTML5\n', 'font_name': ['QECAAA+IRANSans'], 'font_sieze': [11], 'text_color': [[0.976470588, 0.650980392, 0.043137254]]}



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
    
def get_font_color(element):
    error_count = 0
    color_list = []
    for text_line in element:
        try:
            for character in text_line:
                if isinstance(character, LTChar):
                    if char['non_stroking_color'] not in color_list:
                        color_list.append(char['non_stroking_color'])
        except:
            error_count += 1 
    return color_list


# # with open(file_path, 'rb') as scr_file:
#     with pdfplumber.PDF(scr_file) as pdf_file:
#         for page_layout, char in zip(extract_pages(scr_file), pdf_file.chars):
#             for element in page_layout:
#                 if isinstance(element, LTTextBoxHorizontal):
#                     result[cc] = {
#                         "x0": round(element.x0),
#                         "y0": round(element.y0),
#                         "x1": round(element.x1),
#                         "y1": round(element.y1),
#                         "page_number": page_number,
#                         "content": element.get_text(),
#                         'font_name':get_font_name(element),
#                         'font_sieze':get_font_size(element),
#                         'text_color':get_font_color(element),
#                     }
                    
#                     # result[cc].update(font_list)
#                     print(result[cc])
#                     font_detail.clear()
#                     result.clear()
#                 cc += 1





def finder(box):
    cc=0
    with open(file_path, 'rb') as scr_file:
        with pdfplumber.PDF(scr_file) as pdf_file:
            for page_layout, char in zip(extract_pages(scr_file), pdf_file.chars):
                for element in page_layout:
                    if isinstance(element, LTTextBoxHorizontal):
                        result[cc] = {
                            "x0": round(element.x0),
                            "y0": round(element.y0),
                            "x1": round(element.x1),
                            "y1": round(element.y1),
                            "page_number": page_number,
                            "content": element.get_text(),
                            'font_name':get_font_name(element),
                            'font_sieze':get_font_size(element),
                            'text_color':get_font_color(element),
                        }
                        if result[cc]["x1"] == box["x1"] and result[cc]["font_name"] == box["font_name"]:
                            print(result[cc]['content'])
                        
                        # result[cc].update(font_list)
                        # print(result[cc])
                        font_detail.clear()
                        result.clear()
                    cc += 1



box = {'x0': 284, 'y0': 335, 'x1': 312, 'y1': 343, 'page_number': 1, 'content': 'HTML5\n', 'font_name': ['BAAAAA+IRANYekanWeb'], 'font_sieze': [8], 'text_color': [(1, 1, 1)]}
#  and result[cc]["font_name"] == box["font_name"] and result[cc]['font_sieze'] == box["font_sieze"]
section_box = {'x0': 528, 'y0': 541, 'x1': 563, 'y1': 554, 'page_number': 1, 'content': 'ﻣﻬﺎرت ﻣﻬﺎرت\n', 'font_name': ['QJCAAA+IRANSans-Bold'], 'font_sieze': [13], 'text_color': [[0.976470588, 0.650980392, 0.043137254]]}
item_box = {'x0': 494, 'y0': 498, 'x1': 529, 'y1': 509, 'page_number': 1, 'content': 'HTML5\n', 'font_name': ['QECAAA+IRANSans'], 'font_sieze': [11], 'text_color': [[0.976470588, 0.650980392, 0.043137254]]}



finder(section_box)