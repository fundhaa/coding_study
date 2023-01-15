import sys
from collections import deque
sys.stdin = open("input.txt", "rt")

deq = deque()
n, m = map(int, input().split())

for i in range(n):
    deq.append(i+1)
cnt=1
while len(deq)>1:
    if cnt==m:
        deq.popleft()
        cnt=1
    else:
        deq.append(deq.popleft())
        cnt+=1

print(deq[0])