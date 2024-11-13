def my_zip(a):
    print(a)
    return


a=[n for n in input().split()]
b=[n for n in input().split()]
c=[n for n in input().split()]
strct="false"
if(len(a)==len(b) and len(b)==len(c)):
    strct="true"

my_zip(strct)