from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LTTextBoxHorizontal, LTRect, LTTextBox, LTFigure, LTLayoutContainer, LTPage
import pdfplumber



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
                if isinstance(element, LTTextBoxHorizontal):
                    # isinstance(element, LTRect) or
                    result[cc] = {
                        "x0": round(element.x0),
                        "y0": round(element.y0),
                        "x1": round(element.x1),
                        "y1": round(element.y1),
                        "page_number": page_number,
                        "text": element.get_text(),
                        "analyze": element.analyze,
                    }
                    print(result)
                    # print(dir(element))
                    cc += 1
                    result.clear()
            page_number += 1
        document.close()
        return result



# get_boxes(file_path)