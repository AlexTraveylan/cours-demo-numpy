from pathlib import Path
import numpy as np

DATA1_PATH = Path(__file__).parent / "data1.txt"
DATA2_PATH = Path(__file__).parent / "data2.txt"

numpy_array_to_write = np.random.randint(0, 10_000, size=(100))


with open(DATA1_PATH, "w") as f:
    numpy_array_to_write.tofile(f, sep=",")

numpy_array_to_write = np.random.randint(0, 10_000, size=(10, 10))

with open(DATA2_PATH, "w") as f:
    for row in numpy_array_to_write:
        f.write(",".join(map(str, row)) + "\n")
