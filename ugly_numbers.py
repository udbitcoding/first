class solution:

    def Ugly(self, num):
        self.num=num

        if num==0: 
            return False
        for f in [2,3,5]:
            while num%f==0:
                num/=f
            if num == 1:
                return True

num = int(input())
o = solution()
print(o.Ugly(num))