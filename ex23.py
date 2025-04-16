list1 = [1,5,12,2]

def listToStr(list1):
    line = ""
    if len(list1)>0:
        for i in list1:
            line+=str(i)+" "
        return line
    else:
        print("Error")
        return

print(listToStr(list1))