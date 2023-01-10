import sys
sys.stdin=open("input.txt", "rt")
n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]
a = int(input())
b = [list(map(int, input().split())) for _ in range(a)]


for i in range(a):
    if b[i][2] > n:
        b[i][2]=b[i][2]%n
    if b[i][1] == 0:
        m[b[i][0]-1] = m[b[i][0]-1][b[i][2]:n] + m[b[i][0]-1][0:b[i][2]]
    else:
        m[b[i][0]-1] = m[b[i][0]-1][n-b[i][2]:n] + m[b[i][0]-1][0:n-b[i][2]]
print(m)
'''
for i in range(a):
    h, t, k = map(int, input().split())
    if t==0:
        m[h-1].append(m[h-1].pop(0))
    else:
        m[h-1].insert(0, m[h-1].pop())
'''

s=0
e=n-1
sum=0
for i in range(n):
    for j in range(s, e+1):
        sum+=m[i][j]
        print(m[i][j], end= " ")
    if i<n//2:
        s+=1
        e-=1
    else:
        s-=1
        e+=1
    print()
print(sum)
