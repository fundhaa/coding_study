import sys
sys.stdin = open("input.txt", "rt")

from collections import deque
ref = input()
dq = deque()
n = int(input())
for i in range(n):
    sample = input()
    dq = deque(ref)
    for x in sample:
        if x in dq:
            if x != dq.popleft(): # 이게 순서가 통과되는지 안되는지 보는 것
                print(dq)
                print("#%d NO" %(i+1))
                break
    else:
        if len(dq)==0:
            print("#%d YES" %(i+1))
        else:
            print("#%d NO" % (i + 1))