
class Solution:
    def searchInsert(self, nums, target):
        self.nums = nums
        self.target = target
        lens = len(nums)
        if(lens == 0): return 0

        for i,n in enumerate(nums):
            if(n >= target):
                return i

        return lens

nums =[1,5,3,6,4]
target =6
O = Solution()
print(O.searchInsert(nums,target))