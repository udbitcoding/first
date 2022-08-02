class Solution(object):
    def singleNumber(self, nums):
        self.nums = nums
        res = 0
        for x in nums:
            res ^= x
        return res
nums = [4,1,2,1,2]
o=Solution()
print(o.singleNumber(nums))
