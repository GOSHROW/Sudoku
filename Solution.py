import time

class BackTrackSolution:

    def __init__(self, paraMatrix):

        self.sudokuMatrix = []

        for row in paraMatrix:
            elements = []
            for element in row:
                elements.append(element)
            self.sudokuMatrix.append(elements)
        
        print("Solution starts processing . . . ")
        self.timeStart = time.time()
        self.boolMat = [[False for i in range(9)] for j in range(9)]

        self.assertDim()
        self.createBoolMatrix()

        self.trial = [[1 for i in range(self.r)] for j in range(self.c)]
        self.x, self.y = 0, 0

        self.__mainWorking()
        ob = self.__checkWorking()

    def __checkWorking(self, paraMatrix):
        try:
            self.assertDim()
        except:
            return (False, [])
        if self.y < 0:
            return (False, [])
        return self.sudokuMatrix


    def assertDim(self):
        
        r, c = len(self.sudokuMatrix), len(self.sudokuMatrix[0])
        assert (r ** 0.5)//1 == r ** 0.5 and r == c, "Improper Dimensions"
        t = int((r ** 0.5) // 1)
        self.r = r
        self.c = c
        self.subRC = (t, t)

    def createBoolMatrix(self):
        for x in range(self.r):
            for y in range(self.c):
                if self.sudokuMatrix[y][x] != 0:
                    self.boolMat[y][x] = True

    def inc(self, xx, yy):
        xx += 1
        if xx >= self.r:
            xx = 0
            yy += 1
        return xx, yy

    def dec(self, xx, yy):
        xx -= 1
        if xx < 0:
            xx = 8
            yy -= 1
        return xx, yy

    def printMat(self):
        for i in range(len(self.sudokuMatrix)):
            print(self.sudokuMatrix[i], sep = " ", end = "\n")
        print("\n Finished up in {} seconds".format(time.time() - self.timeStart))

    def checkVal(self, li):
        rets = []
        for ret in li:
            if ret != 0:
                if ret in rets:
                    return False
                else:
                    rets.append(ret)
        return True

    def checkRow(self, rowIndex):
        li = self.sudokuMatrix[rowIndex]
        return self.checkVal(li)

    def checkCol(self, colIndex):
        li = []
        for i in range(self.r):
            li.append(self.sudokuMatrix[i][colIndex])
        return self.checkVal(li)

    def checkSquare(self, square):
        li = []
        squareZ = []
        for i in range(self.r * self.c):
            squareZ.append(((i % self.subRC[0]), (i // self.subRC[1])))
        
        squareX, squareY = squareZ[square]

        for y in range(squareY * self.subRC[0], squareY * self.subRC[0] + self.subRC[1]):
            for x in range(squareX * self.subRC[0], squareX * self.subRC[0] + self.subRC[1]):
                li.append(self.sudokuMatrix[y][x])
        return self.checkVal(li)



    def __mainWorking(self):
        while self.boolMat[self.y][self.x]:
            self.x, self.y = self.inc(self.x, self.y)
        
        if self.y >= self.c:
            self.printMat()
            exit()

        while True:
            self.sudokuMatrix[self.y][self.x] = self.trial[self.y][self.x]

            valid = True
            for i in range(self.c):
                valid = valid and self.checkRow(i) and self.checkCol(i) and self.checkSquare(i)

            if valid:
                self.x, self.y = self.inc(self.x, self.y)
                if self.y >= self.r:
                    self.printMat()
                    exit()
                while self.boolMat[self.y][self.x]:
                    self.x, self.y = self.inc(self.x, self.y)
                    if self.y >= self.r:
                        self.printMat()
                        exit()
            
            else:
                while True:
                    if self.trial[self.y][self.x] == 9:
                        self.trial[self.y][self.x] = 1
                        self.sudokuMatrix[self.y][self.x] = 0
                        self.x, self.y = self.dec(self.x, self.y)
                        
                        if self.y < 0:
                            print("Does not have a proper solution\n")
                            self.printMat(self.sudokuMatrix, self.boolMat)
                            exit()

                        while self.boolMat[self.y][self.x]:
                            self.x, self.y = self.dec(self.x, self.y)
                            if self.y < 0:
                                print("Does not have a proper solution\n")
                                self.printMat(self.sudokuMatrix, self.boolMat)
                                exit()
                    else:
                        self.trial[self.y][self.x] += 1
                        break



if __name__ == '__main__':

# For testing purposes only,
# Run Code by entering your own Sudoku Matrix in grid
# and by python3 Solution.py

    grid = []
    grid.append([3, 0, 6, 5, 0, 8, 4, 0, 0])
    grid.append([5, 2, 0, 0, 0, 0, 0, 0, 0])
    grid.append([0, 8, 7, 0, 0, 0, 0, 3, 1])
    grid.append([0, 0, 3, 0, 1, 0, 0, 8, 0])
    grid.append([9, 0, 0, 8, 6, 3, 0, 0, 5])
    grid.append([0, 5, 0, 0, 9, 0, 6, 0, 0])
    grid.append([1, 3, 0, 0, 0, 0, 2, 5, 0])
    grid.append([0, 0, 0, 0, 0, 0, 0, 7, 4])
    grid.append([0, 0, 5, 2, 0, 6, 3, 0, 0])
    ob = BackTrackSolution(grid)