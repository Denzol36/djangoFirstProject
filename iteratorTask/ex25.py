matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [11, 3, 5],
    [7, 14, 2],
    [6, 9, 8]
]

for lst1,lst2 in zip(matrix1,matrix2):
    print()
    for itm1,itm2 in zip(lst1,lst2):
        sum = 0
        sum += itm1 + itm2
        print(sum, end = "\t")

print()