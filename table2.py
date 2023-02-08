
#rint("Table does not exist")

while 1:
    n=int(input("donner un entier [5..30]"))
    if n in range(5,31):break
    if n>=5 and n<=30:break
l=[]
l1=[]
for i in range(n):
    while 1:
        k=int(input("donner un element de la liste:"))
        if k %2==0:break
    l.append(k)
for j in l:
    if j not in l1:
        l1.append(j)
print(l)
print(l1)
