class Solution(object):
    def smallestDivisor(self, nums, threshold):
        for i in range(1,max(nums)):
            total = 0
            for j in range(len(nums)):
                if (nums[j]/i != nums[j]//i):
                    total += (nums[j]//i)+1
                else: total += nums[j]//i
            if total <= threshold:
                return i
            
            


print(Solution().smallestDivisor([19],5))