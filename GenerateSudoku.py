from GenerateFilled import GenerateFilled
import numpy.random as npr

class Gen:

    def __init__(self, dim, numberVacant):
        self.dim = dim
        self.numberVacant = numberVacant
        self.sudokuMatrix = []
        assert self.numberVacant <= (self.dim ** 2), "Improper Input, Not enough Cells to Vacate"

    def FisherYates(self): 
        arr = list(range(self.dim ** 2))
        for i in range(self.dim ** 2 - 1, 0, -1):
            j = int(npr.uniform(0, i + 1, 1)[0])
            arr[i], arr[j] = arr[j], arr[i]
        return arr

    def remove(self):
        self.sudokuMatrix = GenerateFilled(self.dim).getGenerated()
        randSequence = self.FisherYates()[:self.numberVacant]
        while len(self.sudokuMatrix) == 0:
            self.sudokuMatrix = GenerateFilled(self.dim).getGenerated()
        for i in randSequence:
            x, y = i // self.dim, i % self.dim
            # print(x, y)
            self.sudokuMatrix[x][y] = 0
        return self.sudokuMatrix

if __name__ == '__main__':
# For testing purposes only,
# Run Code by entering your own
# Specifications as Parameters to Gen()
# and by python3 GenerateSudoku.py
    ob = Gen(4, 10).remove()
    for i in ob :
        print(i, sep = " ")