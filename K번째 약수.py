import sys
sys.stdin=open("input.txt", "rt")
n,k = map(int, input().split())
# 내 풀이
a = []
for i in range(1, n+1):
    if n%i==0:
        a.append(i)
try: print(a[k-1])
except : print(-1)

# 강사 풀이
cnt = 0
for i in range(1, n+1):
    if n%i==0:
        cnt += 1
    if cnt==k:
        print(i)
        break
else:
    print(-1)