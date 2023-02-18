import sys
sys.stdin = open("input.txt", "rt")

from collections import deque
import time

arr=list()
for _ in range(7):
    arr.append(list(map(int, input().split())))
chk = [[0 for _ in range(7)] for _ in range(7)]
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

dQ = deque()
dQ.append((0, 0))
arr[0][0]=1
while dQ:
    tmp = dQ.popleft()
    for i in range(4):
        x = tmp[0]+dx[i]
        y = tmp[1]+dy[i]
        if 0<=x<=6 and 0<=y<=6 and arr[x][y]==0:
            arr[x][y]=1
            dQ.append((x, y))
            chk[x][y] = chk[tmp[0]][tmp[1]]+1

if chk[6][6]==0:
    print(-1)
else:
    print(chk[6][6])


'''
while dQ:
    tmp = dQ.popleft()
    #print(dQ)
    if tmp==(6,6):
    #    print(cnt)
        break
    for i in range(4):
        x = dx[i]
        y = dy[i]
        if tmp[0]+x>=0 and tmp[0]+x<=6 and tmp[1]+y>=0 and tmp[1]+y<=6:
            if arr[tmp[0]+x][tmp[1]+y]==0:
                dQ.append((tmp[0]+x, tmp[1]+y))
                #print(tmp)
                chk[tmp[0]+x][tmp[1]+y]=chk[tmp[0]][tmp[1]]+1
     #           cnt+=1
'''
