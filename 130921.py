a = [2,3,9,1,27,7,41,85,16,60,64,293,90,56]
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        if a[i] > a[j]:
            a[i],a[j] = a[j],a[i]
print(a)