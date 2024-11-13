import math
print(math.sqrt(9))

a=float(input("enter the first sides:"))
b=float(input("enter the second side:"))
c=float(input("enter the third side:"))
p=(a+b+c)
print(" the perimeter of triangle is ",p)
print("     ................AREA .........")
s=(a+b+c)/2
print(s)
d=s*(s-a)*(s-b)*(s-c)



print("the area of triangle is : ",math.sqrt(d))
x=math.degrees(math.acos((b**2+c**2-a**2)/(2*b*c)))
y=math.degrees(math.acos((a**2+c**2-b**2)/(2*a*c)))
z=math.degrees(math.acos((a**2+b**2-c**2)/(2*a*b)))
print(x,y,z)

