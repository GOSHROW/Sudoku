from Solution import BackTrackSolution
import numpy.random as npr

def generator(dim):
    
    assert (dim ** 0.5) // 1 == (dim ** 0.5), "Improper Dimensions"
    sudokuMat = []
    
    for i in range(dim):
        rowZero = []
        for j in range(dim):
            rowZero.append(0)
        sudokuMat.append(rowZero)
    
    rootDim = int((dim ** 0.5) // 1)

    squareZ = []
    for i in range(rootDim * rootDim):
        squareZ.append(((i % rootDim), (i // rootDim)))


    for i in range(0, dim, rootDim):
        randomList = npr.permutation(list(range(1, dim + 1)))
        for j in range(len(squareZ)):
            j_0 = squareZ[j][0]
            j_1 = squareZ[j][1]
            sudokuMat[j_0 + i][j_1 + i] = randomList[j]
    
    return sudokuMat

def getGenerated(dim):
    obDiagonalFilled = generator(dim)
    obSolved = BackTrackSolution(obDiagonalFilled)
    print(type(obSolved.ob))


if __name__ == '__main__':
    getGenerated(9)