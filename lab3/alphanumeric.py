


s=str(input("Enter your string:"))
b=True
for i in s:
    if((ord(i)<=57 and ord(i)>=48) or (ord(i)<=90 and ord(i)>=65) or (ord(i)<=122 and ord(i)>=97)):
        continue
    else:
        b=False
        break
if(b==True):
    print("TRUE")
else:
    print("FALSE")