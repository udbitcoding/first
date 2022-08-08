


class Solution:
    def sumOfUnique(self, nums):
        self.nums=nums
        ans=[]
        for i in nums:
            if nums.count(i)==1:
                ans.append(i)
        return sum(ans)

o=Solution()
nums=[1,3,2,1]

print(o.sumOfUnique(nums))