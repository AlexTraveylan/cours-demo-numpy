import numpy as np
from pathlib import Path

FILE1_PATH = Path(__file__).parent / "file1.csv"
FILE2_PATH = Path(__file__).parent / "file2.csv"


# read the first file
file1_array = np.genfromtxt(FILE1_PATH, delimiter=",")
print(file1_array)

# read the second file
file2_array = np.genfromtxt(FILE2_PATH, delimiter=",")
print(file2_array)
