print("Star-Patterns using While Loop")
# ***
# ***
# ***

n=int(input("Enter the Number of Rows:"))

# i - rows 
# j - Columns 

i = 1
while(i<=n):
    j=1
    while(j<=n):
        print("*",end=" ")
        j+=1
    print()   
    i+=1

