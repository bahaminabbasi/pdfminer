from pdfminer.high_level import extract_pages

def first_box_position():
        """gets a list of positions(x0,x1,y0,y1)"""
        position_list = []
        for page_layout in extract_pages('./pdf_files/right-blue-2.pdf'):
            for element in page_layout:
                if str(element.__class__)=="<class 'pdfminer.layout.LTTextBoxHorizontal'>":
                    strElement = str(element)
                    for i in strElement:
                        if i==" ":
                            start=strElement.index(i)+1
                            end=len(strElement)-1
                        else:
                            continue
                    resultElement = strElement[start:end]
                    position_list.append(((resultElement.replace("'"," ")).split("  "))[0])
        """split positions and save in a list"""
        splited_position_list = []
        for position in position_list:
            position.replace("'","")
            strSplitedPosList = position.split(",")
            intPosList=[float(i) for i in strSplitedPosList]
            splited_position_list.append(intPosList)
        maxby2List = max([i[3] for i in splited_position_list])
        minbx1List= min([i[0] for i in splited_position_list])
        result = [minbx1List, maxby2List]
        rounded_result = [round(minbx1List), round(maxby2List)]
        return rounded_result

print(first_box_position())