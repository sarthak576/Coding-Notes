print("Star Pattern - Making a Right Angle Triangle: ")
# *
# * *
# * * * 
# i- rows
# j- columns

n = int(input("Enter Favourite Number of Rows: "))
i=1
while(i<=n):
    j=1
    while(j<=i):
        print("*",end=" ")
        j=j+1 
    i=i+1  
    print()  
    
      
   