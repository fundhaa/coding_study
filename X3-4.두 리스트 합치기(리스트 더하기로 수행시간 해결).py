import sys
sys.stdin = open("input.txt", "rt")
n = int(input())
arr_n = list(map(int, input().split()))
m = int(input())
arr_m = list(map(int,input().split()))
arr = []
x = 0
y=0
'''
while(True):
    if arr_n[0]<=arr_m[0]:
        arr.append(arr_n[0])
        if len(arr_n)>1:
            arr_n.pop(0)
    else:
        arr.append(arr_m[0])
        if len(arr_m) > 1:
            arr_m.pop(0)
    if len(arr_n)==1 and len(arr_m)==1:
        if arr_n[0] <= arr_m[0]:
            arr.append(arr_n[0])
            arr.append(arr_m[0])
        else:
            arr.append(arr_m[0])
            arr.append(arr_n[0])
        break
'''

while(True):
    if (arr_n[x]<=arr_m[y]):
        arr.append(arr_n[x])
        x+=1
        if x==n:
            arr=arr+arr_m[y:]
            break

    else:
        arr.append(arr_m[y])
        y+=1
        if y==m:
            arr=arr+arr_n[x:]
            break


for x in arr:
    print(x, end=" ")