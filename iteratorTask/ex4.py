number = 90
i = 2
while number!=1:
    if number%i == 0:
        number//=i
        print(i)
    else:
        i+=1