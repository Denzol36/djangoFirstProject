numbers = [0, 5, -3, 0, 8, 12, 0, -7, 4]

maxIndex = 0
maxNumber = 0

for ind,itm in enumerate(numbers):
    if maxNumber<itm:
        maxNumber=itm
        maxIndex=ind
        
print(maxNumber,maxIndex)

