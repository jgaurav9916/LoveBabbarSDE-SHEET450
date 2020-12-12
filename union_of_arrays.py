

def union(arr1,arr2):
    count=0
    i=j=0
    arr1 = list(set(arr1))
    arr2 = list(set(arr2))
    arr1.sort()
    arr2.sort()
    l=[]
    n1=len(arr1)
    n2=len(arr2)
    while i < n1 and j < n2:
        if arr1[i] < arr2[j]:
            l.append(arr1[i])
            i=i+1
        elif arr1[i] > arr2[j]:
            l.append(arr2[j])
            j=j+1
        else:
            l.append(arr1[i])
            i=i+1
            j=j+1
    while i < n1:
        l.append(arr1[i])
        i=i+1
    while j < n2:
        l.append(arr2[j])
        j=j+1
    x=len(l)
    return x
for t in range(int(input())):
    a = [int(x) for x in input().strip().split()]
    n,m = a[0],a[1]
    arr1 =  [int(x) for x in input().strip().split()]
    arr2 =  [int(x) for x in input().strip().split()]
    print(union(arr1,arr2))