import pdfplumber
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTChar


with open('./pdf_files/jobi-1.pdf', 'rb') as scr_file:
    with pdfplumber.PDF(scr_file) as pdf_file:
        for page_layout, char in zip(extract_pages(scr_file), pdf_file.chars):
            for element in page_layout:
                if isinstance(element, LTTextContainer):
                    for text_line in element:
                        for character in text_line:
                            if isinstance(character, LTChar):
                                print(element.get_text())
                                # print(f"Font Name: {character.fontname}")
                                # print(f"Font Size: {character.size}")
                                print(f"Stroking Color: {char['stroking_color']}")
                                # print(f"Non_stroking Color: {char['non_stroking_color']}")
                                # print('\n\n')