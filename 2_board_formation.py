import cv2
import pytesseract
from PIL import Image
import numpy as np
import os
import csv

# Path to the Tesseract executable (update this path if necessary)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Config path
current_directory = os.path.dirname(os.path.abspath(__file__))
folder_name = 'split_cell'
folder_path = os.path.join(current_directory, folder_name)

# Data handling
matrix = []

for i in range(9):
    row = []
    for j in range(9):
        image_path = f'./cell_{i}{j}.png'
        image = cv2.imread(os.path.join(folder_path, image_path))
        
        # Image preprocess
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, thresholded_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        
        # Noise removal
        kernel = np.ones((3, 3), np.uint8)
        clean_image = cv2.morphologyEx(thresholded_image, cv2.MORPH_OPEN, kernel, iterations=2)

        # Perform OCR
        custom_config = r'--psm 6 outputbase digits'
        recognized_digit = pytesseract.image_to_string(clean_image, config=custom_config)

        # Post-process
        recognized_digit = ''.join(filter(str.isdigit, recognized_digit))

        if recognized_digit == '':
            row.append(0)
        else: 
            row.append(int(recognized_digit))
    matrix.append(row)

# Write result to csv file
with open('board.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(matrix)

print('Successfully write board to board.csv!')