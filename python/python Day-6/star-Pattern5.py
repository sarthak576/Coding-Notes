print("Star Pattern - Making a Right Angle Triangle: ")
# * * *
#  * *
#   *
# i- rows
# j- columns

n = int(input("Enter Favourite Number of Rows: "))
i=n
while(i>0):
    j=1
    while(j<=n-i):
        print(" ",end=" ")
        j=j+1
    k=1
    while(k<i*2):
        print("*",end=" ")
        k=k+1
   
    i=i-1  
    print()  
    
      
   