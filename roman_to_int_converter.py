from re import I
from numpy import outer


class solution():
    def romantoint(self,s):
        self.strint=s

        D={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

        result=0
        privous='I'

        for i in s[::-1]:
            if D[i]<D[privous]:
                result -= D[i]
            else:
                result += D[i]
            privous = i
        return result

s='X'
o=solution()
print(o.romantoint(s))
