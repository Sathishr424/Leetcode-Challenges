class Solution(object):
    def combinationSum(self, candidates, target):
        ret = []
        for l in range(0,len(candidates)):
            match = []
            cnt = 0
            for k in range(l,len(candidates)):
                for i in range(k,len(candidates)):
                    for j in range(i,len(candidates)):
                        while cnt < target:
                            if (match not in ret): match.append(candidates[j])
                            cnt += candidates[j]
                            print(cnt, match)
                        if (cnt == target):
                            if (match not in ret): ret.append(match[:])
                            cnt -= match.pop()
                        elif (cnt > target):
                            cnt -= match.pop()
                            if (j==len(candidates)-1):
                                cnt -= match.pop()
            
        return ret

print(Solution().combinationSum([2,2,5,5,3,6,7],7))
