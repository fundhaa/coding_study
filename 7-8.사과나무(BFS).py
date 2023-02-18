import sys
from collections import deque
import time
sys.stdin = open("input.txt", "rt")

n = int(input())
arr = list()
for _ in range(n):
    arr.append(list(map(int, input().split())))
st = time.time()
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
print(time.time()-st)


#BFS
st = time.time()
dQ = deque()
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
chk = [[0 for _ in range(n)] for _ in range(n)]
chk[n//2][n//2]=1
sum = 0
sum+=arr[n//2][n//2]
dQ.append((n//2, n//2))

L=0

while True:
    if L>=n//2:
        break
    size = len(dQ)
    for i in range(size):
        tmp = dQ.popleft()
        for j in range(4):
            if chk[tmp[0]+dx[j]][tmp[1]+dy[j]]==0:
                chk[tmp[0]+dx[j]][tmp[1]+dy[j]]=1
                sum+=arr[tmp[0]+dx[j]][tmp[1]+dy[j]]
                dQ.append((tmp[0]+dx[j],tmp[1]+dy[j]))
    L+=1
print(sum)
print(time.time()-st)