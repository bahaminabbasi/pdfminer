from pdf2image import convert_from_path
from pathlib import Path





file_path = "./pdf_files/others/eng1.pdf"
# file_path = "./pdf_files/jobi-1.pdf"
# file_path = "./pdf_files/right-blue-1.pdf"

import fitz

doc = fitz.open(file_path)
page = doc[0]
height = page.rect.height
width = page.rect.width
print(width)
print(height)
ratio = height/width
print(ratio)
new_height = 600 * ratio


images = convert_from_path(
    file_path,
    output_folder='./images/',
    fmt='JPEG',
    size=(600,new_height)
    )





# def pdf_to_image():
#         # the package that helping pdf2image to extract images
#         # poppler_path = os.path.join(BASE_DIR, 'static/poppler-22.04.0/library/bin')

#         # the pdf file path
#         file_path = './pdf_files/jobi-1.pdf'

#         # getting just file name for multiple tasks
#         file_name = Path(file_path).stem

#         # the path that pages are going to save in
#         # if doesn't exists it will create one
#         images_path = './images/'
#         # Path(images_path).mkdir(parents=True, exist_ok=True)
#         output_folder = images_path
#         convert_from_path(pdf_path=file_path, output_folder=output_folder, fmt='JPEG')

# pdf_to_image()