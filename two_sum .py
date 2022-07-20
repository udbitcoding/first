# two sum

class Solution(object):
    
    def twoSum(self, nums, target):
    
        self.nums= nums
        self.targert = target

        values={}
        for i , value in enumerate(nums):
            r_num = target - value

            if r_num in values:
                return[values[r_num],i]
            else:
                values[value] = i
nums=[2,5,6,8]
n=int(input())
n1=Solution()
print(n1.twoSum(nums,n))
        