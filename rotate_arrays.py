
def rotate(arr,n):
    arr = arr[n-1:] + arr[:n-1]
    return arr

for t in range(int(input())):
    n = int(input())
    arr = [int(x) for x in input().strip().split()]
    l = rotate(arr,n)
    for i in l:
        print(i,end=" ")
    print()