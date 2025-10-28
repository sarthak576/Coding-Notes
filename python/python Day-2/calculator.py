
print( "Welcome to My program 'Calcinator'")

print("Give me 2 numbers and setect options for calculation")


n1=int(input("Enter 1st number: "))
n2=int(input("Enter 2nd number: "))

option = int(input("choose any one option multiple options: "))

print("Option  1-Add,\n\t2-Subtract,\n\t3-Multiply,\n\t4-Divide\n\t")


if(option==1):
    print(f"After Adding {n1} and {n2}\nfound result: ",n1+n2)

elif(option==2):
    print(f"After Subtracting {n1} and {n2}\nAmazing reults: ",n1-n2)
elif(option==3):
    print(f"Wow I will Multiply {n1}&{n2} Quikly.\nYour Answer is: ",n1*n2)    

else:
    print(f"Its not a complex calculaion, Just {n1} divided by {n2}\nThis is the answer: ",n1/n2)    


