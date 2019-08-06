n=int(input())
a=list(input().split())
for i in range(n):
    l=i+1
    for j in range(l,n):
        m=l+1
        for k in range(m,n):
            if((int(a[i])+int(a[j]))==int(a[k])):
                if ((int(a[i]) < int(a[j]))):
                    if(int(a[j]) < int(a[k])):
                        print(a[i],a[j],a[k])

