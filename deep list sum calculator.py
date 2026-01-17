def deep_sum(l):
    sum=0
    if len(l)==0:
        return sum
    for i in l:
        if type(i)==int:
            sum+=i
        else:
            sum+=deep_sum(i)
    return sum
print(deep_sum([1, 2, [3, 4]]))
print(deep_sum([1, [2, [3, [4]]]]))      
print(deep_sum([10, [20], 30, [40, [5]]]))
print(deep_sum([1,2,3,4]))
print(deep_sum([]))
