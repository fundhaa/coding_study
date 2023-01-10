import sys
sys.stdin = open("input.txt", "rt")
n = int(input())
m = list(map(int,input().split()))
t = int(input())
m.sort()
for i in range(t):
    m[0] = m[0]+1
    m[n-1] = m[n-1]-1
    m.sort()
print(m[n-1]-m[0])