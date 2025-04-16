list1 = [2,3,6,5]

def printHistogram(list1,sym):
    if len(list1)>0:
        for i in list1:
            print(sym*i)
    else:
        print("Error")
        
printHistogram(list1,'@')