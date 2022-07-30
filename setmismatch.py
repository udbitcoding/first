class Solution:
  def findErrorNums(self, nums):
    for num in nums:
      if nums[abs(num) - 1] < 0:
        duplicate = abs(num)
      else:
        nums[abs(num) - 1] *= -1

    for i, num in enumerate(nums):
      if num > 0:
        return [duplicate, i + 1]

nums=[1,2,2,4]

o = Solution()

print(o.findErrorNums(nums))
	