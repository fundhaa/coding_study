import sys
sys.stdin = open("input.txt", "rt")

n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]

m.sort(key = lambda x : [x[1],x[0]], reverse=True)
h = m[0][0]
w = m[0][1]
cnt = 1

for i in range(1, len(m)):
    if h<=m[i][0] or w<=m[i][1]:
        if h<=m[i][0]:
            h = m[i][0]
        if w<=m[i][1]:
            w = m[i][1]
        cnt+=1
print(cnt)