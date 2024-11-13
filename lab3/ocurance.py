b=str(input("enter the string:"))
c=str(input("enter the charater to check their occurance:"))
a=len(b)

count=0
for i in range(0,a):
    if(b[i]==c):
        count=count+1
print(count)