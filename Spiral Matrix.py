class Solution(object):
    def spiralOrder(self, matrix):
        n,m = len(matrix[0]),len(matrix)
        if m == 0 and n == 0: return []
        ret = [[0]*n for i in range(m)]
        x,y=0,0
        dir = 'r'
        ans = []
        for i in range(n*m):
            ret[y][x] = i+1
            ans.append(matrix[y][x])
            if dir == 'r':
                if x+1 >= n or ret[y][x+1] != 0:
                    dir = 'd'
                    y+=1
                    if y >= m: break
                else: x+=1
            elif dir == 'd':
                if y+1 >= m or ret[y+1][x] != 0:
                    dir = 'l'
                    x-=1
                    if x < 0: break
                else: y+=1
            elif dir == 'l':
                if x-1 < 0 or ret[y][x-1] != 0:
                    dir = 'u'
                    y-=1
                    if y < 0: break
                else: x-=1
            elif dir == 'u':
                if y-1 < 0 or ret[y-1][x] != 0:
                    dir = 'r'
                    x+=1
                    if x >= n: break
                else: y-=1
        return ans
        
        
print(Solution().spiralOrder([[1]]))