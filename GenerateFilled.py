from Solution import BackTrackSolution
import numpy.random as npr

class GenerateFilled:

    def __init__(self, dim):
        self.dim = dim

    def generator(self):
        
        assert (self.dim ** 0.5) // 1 == (self.dim ** 0.5), "Improper self.dimensions"
        sudokuMat = []
        
        for i in range(self.dim):
            rowZero = []
            for j in range(self.dim):
                rowZero.append(0)
            sudokuMat.append(rowZero)
        
        rootDim = int((self.dim ** 0.5) // 1)

        squareZ = []
        for i in range(rootDim * rootDim):
            squareZ.append(((i % rootDim), (i // rootDim)))


        for i in range(0, self.dim, rootDim):
            randomList = npr.permutation(list(range(1, self.dim + 1)))
            for j in range(len(squareZ)):
                j_0 = squareZ[j][0]
                j_1 = squareZ[j][1]
                sudokuMat[j_0 + i][j_1 + i] = randomList[j]
        
        return sudokuMat

    def getGenerated(self):
        obDiagonalFilled = self.generator()
        obSolved = BackTrackSolution(obDiagonalFilled).ob
        return obSolved


if __name__ == '__main__':
# For testing purposes only,
# Run Code by entering your own Sudoku Matrix in parameter
# and by python3 GenerateFilled.py
    ret = GenerateFilled(9).getGenerated()
    print(ret, sep = " ", end = "\n")