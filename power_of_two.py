class Solution:
    def isPowerOfTwo(self, n):
        self.n=n
        if n <= 0:
            return False
        if n == 1:
            return True
        
        while n > 1:
            n /= 2
        return n == 1
n=int(input())
o=Solution()
print(o.isPowerOfTwo(n))