class Solution:
    def strongPasswordChecker(self, s):
        print(len(s))
        changes = 0
        specChange = 0
        repConditions = []
        cond = [False,False,False]
        for i in range(len(s)):
            if i > 0 and i < len(s)-1:
                if s[i-1] == s[i] and s[i] == s[i+1]:
                    if i-1 in repConditions and i-1 > repConditions[len(repConditions)-1]:
                        specChange+=1
                    else:
                        changes += 1
                        repConditions.append(i)
                        repConditions.append(i+1)
            if s[i].islower() and not cond[0]:
                cond[0] = True
            elif s[i].isupper() and not cond[1]:
                cond[1] = True
            elif s[i].isdigit() and not cond[2]:
                cond[2] = True
        condChange = 0
        tmp = changes
        if len(s) > 20:
            if len(s)-changes > 20:
                changes += max(20, (len(s)-changes)) - min(20, (len(s)-changes))
                tmp = 0
            else:
                tmp = (20 - (len(s)-changes))
        for i in cond:
            if not i:
                if tmp > 0:
                    tmp-=1
                else:
                    condChange+=1
        
        if len(s) < 6:
            if len(s)+condChange+changes < 6:
                changes += max(6,(len(s)+condChange)) - min(6,(len(s)+condChange))
                
            
        changes+=condChange
        
        return changes+specChange
            
        
print(Solution().strongPasswordChecker("1234567890123456Baaaaa"))