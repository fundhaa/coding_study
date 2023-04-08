import sys
from collections import deque
sys.stdin = open("input.txt", "rt")

dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
Q = deque()
n = int(input())
bound = [list(map(int, input().split())) for _ in range(n)]
cnt=0
for i in range(n):
    for j in range(n):
        if bound[i][j]==1:
            bound[i][j]=0
            Q.append((i,j))
            while Q: # Q가 빌 때 까지 돌아라
                tmp = Q.popleft()
                for k in range(8):
                    x = tmp[0]+dx[k]
                    y = tmp[1]+dy[k]
                    if 0<=x<n and 0<=y<n:
                        if bound[x][y]==1:
                            bound[x][y]=0
                            Q.append((x,y))
            cnt+=1
print(cnt)
0749303792866