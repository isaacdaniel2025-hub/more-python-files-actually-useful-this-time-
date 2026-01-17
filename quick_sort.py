#you are using python
def pivotr(l) :
    right=[]
    left=[]
    if sorted(l)==l:
        return l
    p=l.pop()
    for i in l:
        if i>p:
            right.append(i)
        else:
            left.append(i)
    k=pivotr(left)+[p]+pivotr(right)
    return k
l=eval(input("Enter list to be sorted"))
l=pivotr(l)
print(l)
