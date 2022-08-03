from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTChar
import re


def font_info_extractor():
    font_list = []
    font_info_dict = {}
    cleared_font_list = []
    error_count = 0
    for page in extract_pages('./pdf_files/jobi-4.pdf'):
        for element in page:
            if isinstance(element, LTTextContainer):
                for text_line in element:
                    try:
                        for char in text_line:   
                            if isinstance(char, LTChar):
                                if char.fontname not in font_list:
                                        # font_name_str = font_list.append(char.fontname)
                                        new_str = re.sub(r'^.*?\+', '', char.fontname)
                                        font_info_dict[new_str] = round(char.size)
                                        if font_info_dict not in font_list:
                                            font_list.append(font_info_dict.copy())
                                        font_info_dict.clear()
                    except:
                        error_count += 1

    # for item in font_list:
    #     ch = '\+'
    #     pattern = ".*" + ch
    #     # new_str = re.sub(pattern, '', str(item))
    #     new_str = re.sub(r'^.*?\+', '', item)
    #     cleared_font_list.append(new_str)
    # # return font_list, error_count, cleared_font_list
    return font_list

print(font_info_extractor())

