n1=10
n2=10
n3=10

def NumberCheck(n1,n2,n3):
    res=n1+n2+n3
    if(n1==n2 and n1==n3):
        return res*3
    else:
        return res

print(NumberCheck(n1,n2,n3))