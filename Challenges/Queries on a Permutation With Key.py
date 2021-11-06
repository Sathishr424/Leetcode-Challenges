class Solution:
    def processQueries(self, queries, m):
        ret = []
        p = [i for i in range(1,m+1)]
        for i in range(len(queries)):
            index = p.index(queries[i])
            ret.append(index)
            p.insert(0,p[index])
            del p[index+1]
        return ret
    
print(Solution().processQueries([3,1,2,1],5))