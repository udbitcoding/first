class solution():
    def contain_dublicate(self,list1):
        self.list1=list1

        a=set()
        for i in list1:
            if i in a:
                return True
            a.add(i)
        return False

list1=[1,2,3,4,1]
s=solution()
print(s.contain_dublicate(list1))