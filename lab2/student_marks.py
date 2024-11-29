a= str(input("Enter the Name: "))
b= int(input("Enter the Roll: "))
c= int(input("Enter the Marks out of 100: "))
g=0
r="Fail"

if (c>=90):
    g=10
    r="OUTSTANDING"
elif (c<90 and c>=80):
    g=9
    r="VERY GOOD"

elif (c<80 and c>=70):
    g=8
    r="GOOD"

elif (c<70 and c>=60):
    g=7
    r="AVERAGE"
elif (c<60 and c>=50):
    g=6
    r="PASS"
elif (c<50):
    g=0
    r="FAIL"

print('Name: ',a)
print('Roll Number: ',b)
print('Marks: ',c)
print('Grade Point: ',g)
print('Remark:',r)