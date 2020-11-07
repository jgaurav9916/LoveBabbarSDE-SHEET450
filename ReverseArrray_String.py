#https://practice.geeksforgeeks.org/problems/reverse-the-string/0#


def reverse(s):
    d=""
    i=len(s)-1
    while i >=0:
        d=d+s[i]
        i=i-1
    return d
for t in range(int(input())):
    s=input()
    print(reverse(s))