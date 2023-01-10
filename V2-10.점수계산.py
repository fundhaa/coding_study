import sys
sys.stdin=open("input.txt", "rt")

n = int(input())
answer = list(map(int, input().split()))
cnt = 0
score = 0
for i in range(n):
    # 1번문제가 맞으면 1점
    # 이전문제 틀리고 답이 맞는 문제는 1점
    # 연속으로 담이 맞는 경우는 점수가 1점씩 추가
    if i==0 and answer[0] == 1:
        cnt=1
        score=score+cnt
        continue
    if i != 0 and i != n-1:
        if answer[i-1]==0 and answer[i] == 1:
            cnt=1
            score=score+cnt
            continue
        if answer[i-1]==1 and answer[i] == 1:
            cnt+=1
            score=score+cnt
            continue
        if answer[i-1]==1 and answer[i]==0:
            cnt=0
            continue
    if i==n-1 and answer[i]==1 and answer[i-1]==0:
        cnt=1
        score=score+cnt
        continue
    if i==n-1 and answer[i]==1 and answer[i-1]==1:
        cnt+=1
        score=score+cnt
        continue
print(score)


강사 풀이
'''
cnt=0
answer = 0
for x in answer:
    if x==1:
        cnt+=1
        score += 1
    else:
        cnt=0
'''