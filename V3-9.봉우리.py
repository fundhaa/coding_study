import sys
sys.stdin=open("input.txt", "rt")
n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]
m.insert(0,[0]*(n+2))
m.insert(n+1,[0]*(n+2)) #  ==  m.append([0]*n)


for i in range(1, n+1):
    m[i].insert(0,0)
    m[i].insert(n+1,0)

sum=0
for i in range(1,n+1):
    for j in range(1,n+1):
        if m[i][j]>m[i-1][j] and m[i][j]>m[i+1][j] and m[i][j]>m[i][j-1] and m[i][j]>m[i][j+1]:
            sum+=1

print(sum)


## 3시 6시 9시 12시 탐색
cnt=0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for i in range(1, n+1):
    for j in range(1, n+1):
        if all(m[i][j]>m[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt+=1

print(cnt)