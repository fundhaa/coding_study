import sys
from collections import deque
import copy
sys.stdin = open("input.txt","rt")

n = int(input())
bound = [list(map(int, input().split())) for _ in range(n)]

Q = deque()
cnt=0
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
k=1
rcnt=0
maxi = 0
mini = 21470000
for i in range(n):
    for j in range(n):
        if maxi<bound[i][j]:
            maxi = bound[i][j]
        if mini>bound[i][j]:
            mini = bound[i][j]
#print(mini, maxi)
while mini<=maxi:
    #print(mini, maxi)
    ref = copy.deepcopy(bound)
    #print(id(ref), id(bound))
    #print(ref, bound)
    rcnt = 0
    for i in range(n):
        for j in range(n):
            if ref[i][j]>mini:
                ref[i][j]=0
                Q.append((i,j))
                while Q:
                    a = Q.popleft()
                    for b in range(4):
                        x = a[0]+dx[b]
                        y = a[1]+dy[b]
                        if 0<=x<n and 0<=y<n and ref[x][y]>mini:
                            ref[x][y]=0
                            Q.append((x, y))
                    #print(Q, mini, end= "  ")
                    #print()
                rcnt+=1
    if rcnt>cnt:
        cnt=rcnt
    #print(cnt)
    mini+=1

print(cnt)