a=[1,2,4,3,2,4,1,3,1]
b={}
for i in a:
    b[i]=a.count(i)
    if b[i]==1:
        b.pop(i)
for j,k in b.items():
    print(j,' - ',k)
