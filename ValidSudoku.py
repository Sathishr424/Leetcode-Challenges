
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
        
    def isValidSudoku(self, board):
        box = [[],[],[],[],[],[],[],[],[]]
        for i in range(len(board)):
            tmpRow = []; tmpColumn = [];
            for j in range(len(board[i])):
                if board[i][j] != '.' and board[i][j] not in tmpColumn: tmpColumn.append(board[i][j])
                elif board[i][j] != '.': return False
                if board[j][i] != '.' and board[j][i] not in tmpRow: tmpRow.append(board[j][i])
                elif board[j][i] != '.': return False
                bIndex = self.getBoxIndex(i,j)
                if board[i][j] != '.' and board[i][j] not in box[bIndex]: box[bIndex].append(board[i][j])
                elif board[i][j] != '.': return False
        return True
    

inp = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
print(Solution().isValidSudoku(inp))