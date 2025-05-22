import cProfile

def sumN(n):
    sum = 0
    for i in range(n+1):
        sum+=i
    return sum

print(sumN(8))
cProfile.run('sum(range(8+1))')