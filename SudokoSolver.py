import random
    
square = [[],[],[],[],[],[],[],[],[]]
col = [[],[],[],[],[],[],[],[],[]]
row = [[],[],[],[],[],[],[],[],[]]
skip = []
totalCnt = 0

class Solution(object):
    def getBoxIndex(self,x,y):
        x+=1;y+=1;
        ret = 0
        tmpX = 9/x
        tmpY = 9/y
        if (tmpX >= 3): ret += 0
        elif tmpX >= 1.5 and tmpX < 3: ret += 1
        else: ret += 2
        
        if (tmpY >= 3): ret += 0
        elif tmpY >= 1.5 and tmpY < 3: ret += 3
        else: ret += 6
        return ret
    
    def getBoxIndexWithVal(self,x,y):
        x+=1;y+=1;
        ret = 0
        tmpX = 9/x
        tmpY = 9/y
        i = 0; j=0;
        if (tmpX >= 3): ret += 0
        elif tmpX >= 1.5 and tmpX < 3: 
            ret += 1
            i = 3
        else: 
            ret += 2
            i = 6
        
        if (tmpY >= 3): ret += 0
        elif tmpY >= 1.5 and tmpY < 3: 
            ret += 3
            j = 3
        else: 
            ret += 6
            j = 6
        
        x-=1;y-=1;
        j = (y-j); i = (x-i)*3;
        return ret, i+j
    
    def getMissingNums(self,arr):
        ret = []
        ind = []
        for i in range(1,10):
            if arr[i-1] == '0': ind.append(i-1)
            if str(i) not in arr: ret.append(str(i))
        return ret, ind
    
    def compareList(self,arr,val):
        ret = []
        for i in val:
            if i not in arr: ret.append(i)
        return ret
    
    def minEmptyCell(self):
        mini = 9
        ret = [0,0]
        isRow = True
        rnd = [0,1,2,3,4,5,6,7,8]
        for i in range(len(rnd)):
            cnt = row[i].count('0')
            if cnt < mini and cnt != 0 and [i,0] not in skip:
                mini = cnt
                ret = [i,0]
        for i in range(len(rnd)):
            cnt = col[i].count('0')
            if cnt < mini and cnt != 0 and [0,i] not in skip:
                mini = cnt
                ret = [0,i]
                isRow = False
        # print(ret)
        return ret, isRow
    
    def checkIfSolved(self):
        for i in row:
            if i.count('0') > 0: return False
        return True
    
    def findTotalSolve(self,arr,find):
        tot = 0
        for i in arr:
            tot += i.count(find)
        return tot
    
    def startSolv(self):
        if (self.checkIfSolved()): return row
        mini,isRow = self.minEmptyCell()
        if (isRow):
            miss,ind = self.getMissingNums(row[mini[0]])
            rMiss = miss
            cMiss = miss
            for i in ind:
                cMiss = self.compareList(col[i], miss)
                if (len(cMiss) == 1):
                    row[mini[0]][i] = str(cMiss[0])
                    col[i][mini[0]] = str(cMiss[0])
                    #FOR SQUARE
                    ind, secondInd = self.getBoxIndexWithVal(mini[0], i)
                    square[ind][secondInd] = str(cMiss[0])
                    #END SQUARE
                    del miss[miss.index(cMiss[0])]
                    continue
                cMiss = self.compareList(square[self.getBoxIndex(mini[0], i)], cMiss)
                if (len(cMiss) == 1):
                    row[mini[0]][i] = str(cMiss[0])
                    col[i][mini[0]] = str(cMiss[0])
                    #FOR SQUARE
                    ind, secondInd = self.getBoxIndexWithVal(mini[0], i)
                    square[ind][secondInd] = str(cMiss[0])
                    #END SQUARE
                    del miss[miss.index(cMiss[0])]
                    continue
            if (len(miss) == len(rMiss)): 
                if (mini not in skip): skip.append(mini)
            else: skip.clear()
        else:
            miss,ind = self.getMissingNums(col[mini[1]])
            rMiss = miss
            cMiss = miss
            for i in ind:
                cMiss = self.compareList(row[i], miss)
                if (len(cMiss) == 1):
                    col[mini[1]][i] = str(cMiss[0])
                    row[i][mini[1]] = str(cMiss[0])
                    #FOR SQUARE
                    ind, secondInd = self.getBoxIndexWithVal(i,mini[1])
                    square[ind][secondInd] = str(cMiss[0])
                    #END SQUARE
                    del miss[miss.index(cMiss[0])]
                    continue
                cMiss = self.compareList(square[self.getBoxIndex(i,mini[1])], cMiss)
                if (len(cMiss) == 1):
                    col[mini[1]][i] = str(cMiss[0])
                    row[i][mini[1]] = str(cMiss[0])
                    #FOR SQUARE
                    ind, secondInd = self.getBoxIndexWithVal(i,mini[1])
                    square[ind][secondInd] = str(cMiss[0])
                    #END SQUARE
                    del miss[miss.index(cMiss[0])]
                    continue
            if (len(miss) == len(rMiss)):
                if (mini not in skip):
                    skip.append(mini)
            else: skip.clear()
        if (len(skip) >= 9): skip.clear()
        try:
            return self.startSolv()
        except RecursionError:
            skip.clear()
            
    def solveSudoku(self, board):
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == '.': col[j].append('0')
                else: col[j].append((board[i][j]))
                if board[i][j] == '.': row[i].append('0')
                else: row[i].append((board[i][j]))
                ind = self.getBoxIndex(i,j)
                if board[i][j] == '.': square[ind].append('0')
                else: square[ind].append((board[i][j]))
        return self.startSolv()

                
    
inp = [['.', '7', '.', '.', '1', '.', '.', '2', '.'], ['4', '.', '8', '6', '.', '.', '.', '.', '.'], ['.', '9', '2', '4', '.', '7', '6', '.', '.'], ['.', '5', '9', '.', '6', '.', '1', '4', '.'], ['8', '.', '.', '.', '.', '.', '.', '.', '7'], ['.', '4', '3', '.', '7', '.', '5', '8', '.'], ['.', '.', '5', '2', '.', '8', '7', '6', '.'], ['.', '.', '.', '.', '.', '3', '4', '.', '2'], ['.', '2', '.', '.', '5', '.', '.', '3', '.']]
sol = Solution().solveSudoku(inp)