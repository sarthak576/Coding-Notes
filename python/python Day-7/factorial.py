print("Hey, I am Facto Funtion!!\n Nice to meet U. BRO!!!")

num = int(input("Hey, Give Me a number To find out factorial: \n"))


def factorial_fn(num):
    if(num<0):
        print("Factorail of negative or 0 Is not Possible....")
        return 0
    elif(num==0 or num==1):
        return 1
    else:
        factorial = 1
        for i in range(1,num+1):
            factorial *=i
        return factorial
        
        
result = factorial_fn(num)
print(f"Okay,For {num} it's factorial could be {result}")