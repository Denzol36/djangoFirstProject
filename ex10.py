dates1 = (2014,7,2)
dates2 = (2014,10,10)

def MonthInDays(i):
    MonthInDay = 0
    if i[1]==2:
        MonthInDay+=(i[1]*28)
    elif i[1]%2==0:
            MonthInDay+=(i[1]*30)
    else:
        MonthInDay+=(i[1]*31)
    return MonthInDay

def Cheker(i):
    if i[1]>0 and i[1]<13 and i[2]>0 and i[2]<32:
        return True
    else:
        return False
    

def main():
    if(Cheker(dates1) and Cheker(dates2)):
        MonthInDay1=MonthInDays(dates1)
        MonthInDay2=MonthInDays(dates2)
        Days1=(dates1[0]*365)+MonthInDay1+dates1[2]
        Days2=(dates2[0]*365)+MonthInDay2+dates2[2]
        print(Days2-Days1)
    else:
        print("Error")

main()

