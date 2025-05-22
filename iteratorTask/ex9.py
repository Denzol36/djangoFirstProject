words = ["level", "world", "madam", "hello", "noon", "python", "radar", "data", "civic", "code"]
count=0

for i in words:
    if i == i[::-1]:
        count+=1

print(count)