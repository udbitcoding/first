
class Solution:
    def isAnagram(self, s, t):
        self.string=s
        self.tstring=t
       
        if len(s) != len(t):
            return False
        elif sorted(s) == sorted(t):
            return True
        else:
            return False

s=input()
t=input()

o=Solution()

print(o.isAnagram(s,t))


