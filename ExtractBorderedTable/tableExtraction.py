import numpy as np
import cv2 as cv
from PIL import Image
from Table import Table
import sys

def isolate_lines(src, structuring_element):
    cv.erode(src, structuring_element, src, (-1, -1)) # makes white spots smaller
    cv.dilate(src, structuring_element, src, (-1, -1)) # makes white spots bigger

MIN_TABLE_AREA = 50 # min table area to be considered a table
EPSILON = 3 # epsilon value for contour approximation
def verify_table(contour, intersections):
    area = cv.contourArea(contour)

    if (area < MIN_TABLE_AREA):
        return (None, None)

    curve = cv.approxPolyDP(contour, EPSILON, True)

    rect = cv.boundingRect(curve) # format of each rect: x, y, w, h

    print("rectangel", rect)
    
    possible_table_region = intersections[rect[1]:rect[1] + rect[3], rect[0]:rect[0] + rect[2]]
    print("table region: ",possible_table_region)
    print()
    (possible_table_joints, _) = cv.findContours(possible_table_region, cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE)
    print("counters table region: ", possible_table_joints)

    if len(possible_table_joints) < 5:
        return (None, None)

    return rect, possible_table_joints


def main():
    path = "img2.png"
    #path = "Exhibit.pdfpage_8.jpg"
    ext_img = Image.open(path)
    ext_img.save("data/target.jpg","JPEG")
    image = cv.imread("data/target.jpg")
    greyscale = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    MAX_THRESHOLD_VALUE = 255
    BLOCK_SIZE = 15
    THRESHOLD_CONSTANT = 0
    filtered = cv.adaptiveThreshold(~greyscale, MAX_THRESHOLD_VALUE,cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, BLOCK_SIZE, THRESHOLD_CONSTANT)

    #cv.imshow("Filtered", filtered)
    SCALE = 10
    horizontal = filtered.copy()
    vertical = filtered.copy()

    h_size = int(horizontal.shape[1]/SCALE)
    h_structure = cv.getStructuringElement(cv.MORPH_RECT, (h_size, 1))
    #cv.imshow("horizontal structuring element",h_structure)
    isolate_lines(horizontal, h_structure)

    v_size = int(vertical.shape[0]/SCALE)
    v_structure = cv.getStructuringElement(cv.MORPH_RECT, (1, v_size))
    #cv.imshow("vertical structuring element", v_structure)
    isolate_lines(vertical, v_structure)

    #cv.imshow("horizontal",horizontal)
    #cv.imshow("vertical", vertical)

    mask = horizontal+vertical

    (contours, _) = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    intersections = cv.bitwise_and(horizontal, vertical)

    #cv.namedWindow("MASK", cv.WINDOW_NORMAL)
    #cv.namedWindow("INTERSECTIONS", cv.WINDOW_NORMAL)

    sm_mask = cv.resize(mask,(960,540))
    sm_intersections = cv.resize(intersections,(960,540))

    #cv.imshow("MASK", sm_mask)
    #cv.imshow("INTERSECTIONS", sm_intersections)

    cv.imshow("MASK", mask)
    cv.imshow("INTERSECTIONS", intersections)

    tables = []
    i=0

    for i in range(len(contours)):

        (rect_cords, table_joints) = verify_table(contours[i], intersections)
        if rect_cords == None or table_joints == None:
            continue

        table = Table(rect_cords[0], rect_cords[1], rect_cords[2], rect_cords[3])

        joint_coords = []
        for i in range(len(table_joints)):
            joint_coords.append(table_joints[i][0][0])
        joint_coords = np.asarray(joint_coords)
        sorted_indices = np.lexsort((joint_coords[:, 0], joint_coords[:, 1]))
        joint_coords = joint_coords[sorted_indices]
        table.set_joints(joint_coords)
        tables.append(table)
    for table in tables:
        print("table: ",table)
         
if __name__ == "__main__":
    main()
