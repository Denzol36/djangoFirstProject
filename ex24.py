numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]

def printUntile237(list1):
    if len(list1)>0:
        for i in list1:
            if i==237:
                break
            elif i%2==0:
                print(i)
            else:
                continue
    else:
        print("eror")
    
printUntile237(numbers)