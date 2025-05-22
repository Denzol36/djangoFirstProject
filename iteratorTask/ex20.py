list1 = [x for x in range(5,20)]
count=0

for ind,itm in enumerate(list1):
    if ind%2==0 and itm>10:
        count+=1
        
print(count)