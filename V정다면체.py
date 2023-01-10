import sys
sys.stdin=open("input.txt", "rt")
n,m = map(int, input().split())
arr = [0]*(n+m+1)
for i in range(1, n+1):
    for j in range(1, m+1):
        arr[i+j]+=1
tmp = -1

for i in range(len(arr)):
    if arr[i]>=tmp:
        tmp = arr[i]
        if tmp==max(arr):
            print(i, end=' ')
