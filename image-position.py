from pdfminer.high_level import extract_pages
from pdfminer.layout import LTImage,LTFigure


def find_image():
    image_info = {}
    rounded_image_info = {}
    image_info_list =[]
    rounded_image_info_list =[]
    for page in extract_pages('./pdf_files/right-blue-2.pdf'):
        for element in page:
            if isinstance(element,LTFigure):
                for image in element:
                    if isinstance(image,LTImage):
                        outputImg = "<Image>\n"
                        outputImg += ("name: %s, " % image.name)
                        outputImg += ("x0: %f, " % image.bbox[0])
                        outputImg += ("y0: %f\n" % image.bbox[1])
                        outputImg += ("x1: %f, " % image.bbox[2])
                        outputImg += ("y1: %f\n" % image.bbox[3])
                        outputImg += ("width1: %f, " % image.width)
                        outputImg += ("height1: %f, " % image.height)
                        outputImg += ("width2: %f, " % image.stream.attrs['Width'])
                        outputImg += ("height2: %f\n" % image.stream.attrs['Height'])
                        image_info = {
                            "box_x0_coor": image.bbox[0],
                            "box_y0_coor": image.bbox[1],
                            "box_x1_coor": image.bbox[2],
                            "box_y1_coor": image.bbox[3],
                        }
                        rounded_image_info = {
                            "box_x0_coor": round(image.bbox[0]),
                            "box_y0_coor": round(image.bbox[1]),
                            "box_x1_coor": round(image.bbox[2]),
                            "box_y1_coor": round(image.bbox[3]),
                        }
                        image_info_list.append(image_info)
                        rounded_image_info_list.append(rounded_image_info)
    return rounded_image_info_list

print(find_image())