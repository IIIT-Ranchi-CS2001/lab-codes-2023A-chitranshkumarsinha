a=str(input("enter the string:"))
b=a.split()
sum=0
for i in b:
    c=i[::-1]
    if(i.lower()==c.lower()):
        sum+=1
print(sum)        