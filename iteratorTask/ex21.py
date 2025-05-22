numbers = [0, 5, -3, 0, 8, 12, 0, -7, 4]

for ind,itm in enumerate(numbers):
    if itm == 0:
        numbers[ind]=ind
        
print(numbers)