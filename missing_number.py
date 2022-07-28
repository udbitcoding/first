class Solution:
    def missingNumber(self, nums):
        self.nums=nums
        
        n = len(nums)
        
        new = set()
        
        for num in nums:
            new.add(num)
        
        for i in range(0, n + 1):
            if i not in new:
                return i
        
nums=[0,1,5,6,4,2]
o = Solution()
print(o.missingNumber(nums))

