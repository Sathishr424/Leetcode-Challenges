
class Solution:
    def powerOfX(self,x):
        cnt = 0
        while x != 1:
            if x%2 == 0: x /= 2
            else: x = (3*x)+1
            cnt += 1
        return cnt
    
    def inSort(self,arr1,arr2,k):
        for i in range(1,len(arr1)):
            for j in range(i,0,-1):
                if arr1[j-1] > arr1[j]:
                    arr1[j-1],arr1[j] = arr1[j],arr1[j-1]
                    arr2[j-1],arr2[j] = arr2[j],arr2[j-1]
                else:break
        return arr2[k-1]
        
    def getKth(self, lo: int, hi: int, k: int) -> int:
        power = []; order = []
        for i in range(lo,hi+1):
            power.append(self.powerOfX(i))
            order.append(i)
        return self.inSort(power,order,k)


# print(Solution().inSort([22,2,5,2,6,3,6,72],[22,2,5,2,6,3,6,72]))
print(Solution().getKth(12,15,2))
print(Solution().getKth(1,1,1))
print(Solution().getKth(7,11,4))
print(Solution().getKth(10,20,5))
print(Solution().getKth(1,1000,777))
print(Solution().getKth(7,463,87))

