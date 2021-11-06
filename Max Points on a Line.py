class Solution:
    def maxPoints(self, points):
        #grid = [[0]*max([i[1] for i in points])]*max([i[0] for i in points])
        if len(points) <= 1: return len(points)
        mx = 0;my = 0;
        for i,j in points:
            if i < 0 or j < 0:
                if i < mx: mx = i
                if j < my: my = j
        if mx < 0 or my < 0:
            for i in range(len(points)):
                points[i][0] += -mx
                points[i][1] += -my
            
        grid = []
        for i in range(max([i[0] for i in points])+1):
            tmp = []
            for j in range(max([i[1] for i in points])+1):
                tmp.append(0)
            grid.append(tmp)
        for i,j in sorted(points):
            grid[i-1][j-1] += 1
        ret = 0
        cnt = 0
        same = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] >= 1:
                    cnt = grid[i][j]
                    for k in range(j+1,len(grid[i])):
                        if grid[i][k] >= 1: cnt += grid[i][k]
                    if cnt > ret:
                        ret = cnt
                        cnt = grid[i][j]
                    
                    for k in range(i+1,len(grid)):
                        if grid[k][j] >= 1: cnt += grid[k][j]
                    if cnt > ret:
                        ret = cnt
                        cnt = grid[i][j]
                        
                    for k in range(1,len(grid)):
                        if i+k < len(grid) and j+k < len(grid[i]) and grid[i+k][j+k] >= 1: cnt += grid[i+k][j+k]
                    if cnt > ret:
                        ret = cnt
                        cnt = grid[i][j]
                        
                    for k in range(1,len(grid)):
                        if i-k >= 0 and j+k < len(grid[i]) and grid[i-k][j+k] >= 1: cnt += grid[i-k][j+k]
                    if cnt > ret:
                        ret = cnt
                        cnt = grid[i][j]
                    
                    if cnt > ret: ret = cnt
                
        return ret
            
        

print(Solution().maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))
print(Solution().maxPoints([[1,2],[4,5]]))
print(Solution().maxPoints([[2,5],[1,2],[7,8],[2,6],[5,7],[3,7],[1,1]]))
print(Solution().maxPoints([[0,0],[1,1],[1,-1]]))
