print("Meet my Areon - Calcualtes area of any 2D shape")

print("Select Any one option -\n\t1-Rectangle,\n\t2-Square,\n\t3-Circle.")
option = int(input("Please Enter Favourite Option: "))


a = int(input("Please Enter 1st Integer: \n"))
b = int(input("Please Enter 2nd Integer: \n"))

def Area_Rectangel(a,b):
   print("Area of rectangle: ",a*b)

def Area_Square(a):
   print("Area of Sqaure: ",a*a)  

def Area_Circle(r):
   print("Area of Circumference: ",3.14*r*r)

if(option==1):
   print(Area_Rectangel(a,b))

elif(option==2):
   print(Area_Square(a))

elif(option==3):
   print(Area_Circle(a))   


else:
   print("Not a valid Option")
   



