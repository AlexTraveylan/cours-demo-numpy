"""
Charge le contenu des fichiers data1.txt et data2.txt et affiche leurs contenus.
"""

import numpy as np

from pathlib import Path

DATA1_PATH = Path(__file__).parent / "files" / "data1.txt"
DATA2_PATH = Path(__file__).parent / "files" / "data2.txt"

# Ecrire le code ici 🔽

data1_array = np.genfromtxt(DATA1_PATH, delimiter=",")
print(data1_array)

data2_array = np.genfromtxt(DATA2_PATH, delimiter=",")
print(data2_array)
