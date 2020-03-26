from Solution import BackTrackSolution

def generator(dim):
    
    assert (dim ** 0.5) // 1 == (dim ** 0.5), "Improper Dimensions"
    sudokuMat = []
    
    for i in range(dim):
        rowZero = []
        for j in range(dim):
            rowZero[j] = 0
        sudokuMat.append(rowZero)
    
    rootDim = int((dim ** 0.5) // 1)

    squareZ = []
    for i in range(dim * dim):
        squareZ.append(((i % rootDim), (i // rootDim)))
    
    