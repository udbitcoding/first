l1 = ["red","fully","blacky","charkat"]
l2=['a',"2","3","4","5","6","7","8","9","10","j","q","r"]
l3=[]
print(l3)
l=[2,15,2,3,15,14,18]
for i in l1:
    for j in l2:
        k=f"{i},{j}"
        l3.append(k.split(","))
j=[]
for i in l:
    j.append([l3[i]])

print(j)
print(j[3][0][1])
if j[0] == j[1]:
    print("parfect")
elif j[0][0][1] == j[1][0][1]:
    print("parfect pair")
else:
    print("nooooooo")