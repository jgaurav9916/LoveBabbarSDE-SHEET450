#code
#Input: -12, 11, -13, -5, 6, -7, 5, -3, -6
#Output: -12 -13 -5 -7 -3 -6 11 6 5
#[-12, -6, -13, -5, -3, -7, 5, 6, 11]

def positive_negative(arr):
    n = len(arr)
    i = 0
    j = n-1
    x=0
    while i < j:
        if arr[i] < x:
            i=i+1
        elif arr[j] > x:
            j=j-1
        else:
            arr[i],arr[j] = arr[j],arr[i]
            i=i+1
            j=j-1
            
            
arr=[-12, 11, -13, -5, 6, -7, 5, -3, -6]
positive_negative(arr)
print(arr)