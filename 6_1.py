#первая
v= [1 , 2, 3, 4,5,1 ,3 ,5, 7 ,7]
k=[]
for i in range (len(v)):
    k.append(i)
print(k)
dicor = dict(zip(v, k))
print(dicor)