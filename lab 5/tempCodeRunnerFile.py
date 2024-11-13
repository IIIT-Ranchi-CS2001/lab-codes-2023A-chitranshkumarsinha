print(sorted_comb)

n = len(comb_nozip)
for i in range(n):
    for j in range(0,n-i-1):
        if(comb_nozip[j]>comb_nozip[j+1]):
            comb_nozip[j],comb_nozip[j+1] = comb_nozip[j+1],comb_nozip[j]
print(comb_nozip)