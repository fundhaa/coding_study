import sys
from collections import deque

sys.stdin = open("input.txt", "rt")

n = int(input())
arr = list()
for _ in range(n):
    arr.append(list(map(int, input().split())))

fref = n//2
rref = n//2
ans = 0

i=0
while i<n:
    if i<=n//2:
        ans += sum(arr[i][fref:rref+1])
        i+=1
        if fref!=0:
            fref-=1
            rref+=1
    else:
        fref += 1
        rref -= 1
        ans+=sum(arr[i][fref:rref+1])
        i+=1

print(ans)

