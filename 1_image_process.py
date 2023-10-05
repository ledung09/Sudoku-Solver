import cv2
import os
 
# Config path
folder_name = 'split_cell'
current_directory = os.path.dirname(os.path.abspath(__file__))
folder_path = os.path.join(current_directory, folder_name)

# Read the image
image_path = './board.png'
image = cv2.imread(image_path)

# Preprocess the image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, thresholded = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
min_table_area = 2000
table_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_table_area]

# Draw outter borders
table_image = image.copy()
cv2.drawContours(table_image, table_contours, -1, (0, 255, 0), 3)

outer_contour = table_contours[0]
x, y, w, h = cv2.boundingRect(outer_contour)
cell_width = w // 9
cell_height = h // 9
cells = []
for i in range(9):
    for j in range(9):
        x1 = x + i * cell_width
        y1 = y + j * cell_height
        x2 = x1 + cell_width
        y2 = y1 + cell_height
        cells.append((x1, y1, x2, y2))

# Draw grids
grid_image = table_image.copy()
for cell_coords in cells:
    x1, y1, x2, y2 = cell_coords
    cv2.rectangle(grid_image, (x1, y1), (x2, y2), (0, 0, 255), 1)

# Write proccessed image to file
cv2.imwrite('proccessed.png', grid_image)

# Seperate image and write to file
for cell_index in range(81):
    x1, y1, x2, y2 = cells[cell_index]
    cell_roi = image[y1:y2, x1:x2]
    # Crop the image to eliminate border 
    border_size = 24
    cropped_image = cell_roi[border_size:-border_size, border_size:-border_size]
    # Save image to png file
    cell_filename = f'cell_{cell_index%9}{cell_index//9}.png'
    cv2.imwrite(os.path.join(folder_path, cell_filename), cropped_image)

print('Successfully split original board to cells!')