import sys
sys.stdin = open("input.txt", "rt")

from collections import deque
n = int(input())
dq = deque()
for _ in range(n):
    dq.append(input())
arr=[]
for _ in range(n-1):
    arr.append(input())

for _ in range(n):
    if dq[0] in arr:
        dq.popleft()
print(dq[0])


