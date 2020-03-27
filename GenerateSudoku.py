from GenerateFilled import GenerateFilled
import random

class Gen:

    def __init__(self, dim, numberVacant):
        self.dim = dim
        self.numberVacant = numberVacant
        self.sudokuMatrix = []
        assert numberVacant <= (self.dim ** 2), "Improper Input, Not enough Cells to Vacate"

    def remove(self):
        self.sudokuMatrix = GenerateFilled(self.dim).getGenerated()
        randSequence = random.sample(range(1, self.dim ** 2), self.numberVacant)
        for i in randSequence:
            x, y = i // self.dim, i % self.dim
            self.sudokuMatrix[x][y] = 0
        return self.sudokuMatrix

if __name__ == '__main__':
# For testing purposes only,
# Run Code by entering your own
# Specifications as Parameters to Gen()
# and by python3 GenerateSudoku.py
    ob = Gen(9, 45).remove()
    for i in ob :
        print(i, sep = " ")