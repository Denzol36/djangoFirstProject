import cProfile
def printWithoutSpace(promt1,promt2):
    print(promt1,promt2, end=" ",sep="")
    
    
printWithoutSpace("sss","ssss")
printWithoutSpace("sss2","ssss2")
print()

cProfile.run('printWithoutSpace("sss2","ssss2")')