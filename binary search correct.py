l=[1,8,7,4,5,2]
for i in range(len(l)):
    insertion_index=i
    current_value=l.pop(i)
    for j in range(i-1,-1,-1):
        if l[j]>current_value:
            insertion_index=j
    l.insert(insertion_index,current_value)
print(l)
x=int(input("Enter element to be searched for: "))
high,low=len(l)-1,0
found=False
while not high<low:
    mid=(high+low)//2
    e=l[mid]
    if e==x:
        print("element is found at index",mid)
        found=True
        break
    elif e<x:
        low=mid+1
    else:
        high=mid-1
if not found:
    print("element not found")
    
