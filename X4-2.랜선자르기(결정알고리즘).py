import sys
sys.stdin = open("input.txt", "rt")

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
'''
mid = sum(arr)//m
i=0
cnt=0
while True:
    cnt+=arr[i]//mid
    i+=1
    if i==n:
        if cnt>m:
            mid = mid+1
        elif cnt==m:
            print(mid)
            break
        else:
            mid= mid-1
        cnt=0
        i=0
'''
# 결정 알고리즘을 사용할 수 있는 문제는, 답이 어떤 범위 안에 있는 문제이다.
#

rt = max(arr)
lt = 1

cnt=0
i=0
mid = (rt+lt)//2
res=[0]
while lt<=rt:
    cnt+=arr[i]//mid
    i+=1
    if i==n:
        if cnt>=m:
            lt=mid+1
            res.append(mid)
        else:
            rt=mid-1
        i=0
        cnt=0
        mid = (rt + lt) // 2

print(max(res))