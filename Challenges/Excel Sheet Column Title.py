from test import Test
import math

alp = list("abcdefghijklmnopqrstuvwxyz")
class Solution:
    def getLetter(self,N):
        n = N
        while n > 26:
            n = int(n/26) + (n%26)
            print(int(n/26), n%26)
        return alp[n]
    
    def convertToTitle(self, n):
        ret = ""
        digit = n-26
        size = 1
        while digit > 26:
            digit = math.sqrt(digit)
            print(digit)
            size+=1
        print(self.getLetter(53))
    
print(Solution().convertToTitle(99994529))