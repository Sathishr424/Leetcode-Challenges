class Solution:
    def checkIfBlue(self,arr,end):
        if not arr[0]: return False
        found = 0
        for i in range(self.index,end):
            if not arr[i] and found == 0: return False
            elif not arr[i] and found == 1: 
                found = 2
                self.index = i-1
            elif arr[i] and found == 0: found = 1
            elif arr[i] and found == 2: return False
        return True
        
    def numTimesAllBlue(self, light: List[int]) -> int:
        ret = 0
        self.index = 0
        blue = [False]*max(light)
        mx = light[0]
        for i in range(len(light)):
            blue[light[i]-1] = True
            if light[i] > mx: mx = light[i]
            if self.index+1 == light[i]-1: 
                self.index = light[i]-1
                ret += 1
            elif self.checkIfBlue(blue,mx): ret += 1
        return ret