#rotation list given number of times
class rotation():
    def rotationlist(self,lists,n):
        self.lists=lists
        self.n=n

        output_list=[]

        for item in range(len(lists)-n,len(lists)):
            output_list.append(lists[item])
        for item in range(0,len(lists)-n):
            output_list.append(lists[item])
        return output_list
      
lists=[1,2,3,4,5,6]
n=3
out=rotation()
print(out.rotationlist(lists,n))
        