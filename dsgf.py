
data=[1,8,6,2,5,4,8,3,7]
l1=0
ans=0
ind1=0
ind2=0
for i in data:
    l2=1
    l1+=1
    for j in data:
        if i>j:
            h=j
        elif i<j:
            h=i
        elif i==j:
            h=i
        ll=abs(l2-l1)
        if ll>0:
            area=h*ll
        else:
            area=0 
        if ans < area:
            ans=area
            ind1=l1
            ind2=l2
        l2+=1
print("Найбільша площа: ",ans)
print("Між ",ind1,"-им і ",ind2,"-им елементом")
