list1 = [x for x in range(10)]
list2 = [x for x in range(10,20)]
sum = 0
for i,j in zip(list1,list2):
    sum += i+j
    
print(sum)