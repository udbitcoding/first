#method 1
str = "welcome to the bitcoding solution!"
words = str.split(' ')
print(words)
words1= words[-1::-1]
print(words1)
str2=' '.join(words1)
print(str2)

#method2
class solution:
    def reversestr(self,str):
        self.str=str
        return ' '.join(reversed(str.split()))

str="welcome to the digital world"
s=solution()
print(s.reversestr(str))

