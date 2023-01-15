import sys
sys.stdin = open("input.txt", "rt")

from collections import deque
deq = deque()

n, m = map(int, input().split())
deq = [(pos, val) for pos, val in enumerate(list(map(int, input().split())))]

deq = deque(deq)
cnt=0
while True:
    tmp=deq.popleft()
    if any(tmp[1]<x[1] for x in deq):
        deq.append(tmp)
    else:
        cnt+=1
        if tmp[0]==m:
            print(cnt)
            break


# index 번호도 같이 저장해야한다.
# linked list 인가.... linked queue? 원형 queue?




# m 번째 진료받는 환자의 우선순의를 출력
'''
for i in range(n):
    while True:
        if deq[0]==max(arr):
            cnt+=1
            if cnt==m:
                print(deq.popleft())
                break
            arr.remove(deq.popleft())
        else:
            deq.append(deq.popleft())

    if cnt==m:
        print()
        break
'''