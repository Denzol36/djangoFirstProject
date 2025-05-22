list1 = [1,2,3,4,5,6]
list2 = [2,3,3,4,5,6]
count = 0

for i,j in zip(list1,list2):
    if i==j:
        count+=1
        
        
print(count)