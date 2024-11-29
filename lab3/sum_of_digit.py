n=int(input("enter the number:"))
sum=0
while(n>0):
    b=n%10
    sum=sum+b
    n=n//10
print("sum of given number is:",sum)    
