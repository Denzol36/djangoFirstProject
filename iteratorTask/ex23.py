lst = [1, 2, 3, 4, 5, 6, 7]
K = 3

K = K % len(lst)
rotated = []
for i in range(len(lst)):
    rotated.append(lst[(i - K) % len(lst)])
print(rotated)
