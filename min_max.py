class solution():
    def minmax(self,nums):
        self.nums=nums

        if len(nums)==1:
                    return nums[0]

        while len(nums)!=1:
            newnums = [-1]*(len(nums)//2)
            for i in range(0,len(nums)//2):
                if i%2==0:
                    newnums[i] = min(nums[2 * i], nums[2 * i + 1])
                else:
                    newnums[i] = max(nums[2 * i], nums[2 * i + 1])
            nums = newnums

        return nums[0]

o=solution()
nums=[2,3,8,6,1,9,5,4]

print(o.minmax(nums))
