import sys
sys.stdin = open("input.txt", "rt")

# deque 사용
'''
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
'''
#dictionary 사용
n = int(input())
p = dict()
for i in range(n):
    word = input()
    p[word] = 1 # word라는 단어가 key로 들어가고 그 key에 해당하는 value는 1로 체크
for i in range(n-1):
    word = input()
    p[word] = 0

# dict 자료형의 item 들은 이렇게 접근
for key, val in p.items():
    if val ==1:
        print(key)
        break

