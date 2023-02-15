import sys
from collections import deque
sys.stdin = open("input.txt", "rt")

axis = 10000
chk = [0]*(axis+1)
ans = [0]*(axis+1)

n, m = map(int, input().split())
chk[n] = 1
ans[n] = 0
dQ = deque()
dQ.append(n)
cnt=0
while dQ: #dQ가 비어있으면 멈춤
    now = dQ.popleft()
    if now==m:
        print(ans[now])
        break
    '''
    for next in(now-1, now+1, now+5): # next는 now-1 now+1 now+5가 순서대로 된다.
        if next>=1:
            if chk[next]==0:
                dQ.append(next)
                chk[next]=1
                ans[next]=ans[now]+1
    '''
    if now==m:
        break
    if chk[now+1] == 0:
        dQ.append(now+1)
        chk[now+1] = 1
        ans[now+1] = ans[now]+1
    if chk[now - 1] == 0:
        dQ.append(now-1)
        chk[now-1] = 1
        ans[now-1] = ans[now]+1
    if chk[now+5] == 0:
        dQ.append(now+5)
        chk[now+5] = 1
        ans[now+5] = ans[now]+1