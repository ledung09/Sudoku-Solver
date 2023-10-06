# Sudoku.com Auto-Solver

## Overview:

This project utilizes computer vision and optical character recognition (OCR) technologies to automatically solve Sudoku puzzles from images. The Sudoku Solver employs OpenCV for image processing, pytesseract OCR for digit recognition, and PyAutoGUI for automating the completion of Sudoku puzzles on the sudoku.com website.

## Technologies Used:

1. OpenCV (cv2):

- OpenCV is used to process the input image of the Sudoku puzzle.
- It separates the puzzle grid into individual cells, making it easier to analyze and recognize digits.

2. Pytesseract:

- Pytesseract is employed for optical character recognition.
- It recognizes digits within each cell of the Sudoku grid, converting them into machine-readable text.

3. PyAutoGUI:

- PyAutoGUI is utilized to automate the input of solved Sudoku digits on the sudoku.com website.
- It simulates keyboard actions to fill in the Sudoku grid and complete the puzzle.

## Setup

1. Clone the repository or download the project files to your local machine:

```
git clone https://github.com/ledung09/Sudoku-Solver.git
```

2. Navigate to the Project Directory:\
   Change your working directory to the project folder:

```
cd Sudoku-Solver
```

3. Install Dependencies:\
   Make sure you have Python installed on your system. This project requires several Python libraries to run. You can install the dependencies using the following command:

```
pip install -r requirements.txt
```

## How to use the Auto-Solver

1. Download the board, simply by `right-click` on the board -> save image as. Remember to save the image in `Sudoku-Solver` folder as `board.png`.
2. Run these 2 files first: `1_image_process.py` and `2_board_formation.py`.\
   This can be done by typing in the terminal:

```
python 1_image_process.py
python 2_board_formation.py
```

3. After a while, 2 files are generated: `processed.png` and `board.csv` and a bunch of images in `split_cell folder`. \
   `processed.png` is still `board.png`, but table border and grids are surrounded by green and red lines. These are used to seperate cells. Cell images are then saved to the folder.\
   `board.csv` is the board, represented like an array, saved inside `csv` file.
4. Before the next step, you need to carefully check, if the board in the `csv` file is exactly like the one on `sudoku.com` or `board.png`. \
   Surprisingly, number `5` is usually the one to be wrongly recognize by OCR!
5. Check if your IDE and Browser are connected by `alt + tab` (this means that if you are either on IDE or Browser, pressing `alt + tab` would be able to switch between one).
6. Run the `3_main.py` file, sit still and enjoy the result :)).

```
python 3_main.py
```
