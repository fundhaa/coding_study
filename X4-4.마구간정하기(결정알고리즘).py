import sys
sys.stdin = open("input.txt", "rt")

def Calc(arr, dist):
    cnt = 1
    tmp = arr[0]
    for x in arr:
        if x-tmp >= dist:
            tmp=x
            cnt+=1
    return cnt

n, m = map(int, input().split())
arr=[]
for _ in range(n):
    arr.append(int(input()))
arr.sort()
# 최대 거리를 mid 로 잡아야 함.
ldx = 1
rdx = max(arr)
res = 0
while ldx<=rdx:
    mid = (ldx+rdx)//m
    if Calc(arr, mid) >= m:
        ldx = mid+1
        res = mid
    else:
        rdx = mid-1
print(res)
