import sys
sys.stdin=open("input.txt", "rt")

## 그리디 문제는 정렬이 생명

n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]
m.sort()
m.sort(key=lambda x : [x[1],x[0]]) # 2번째 인자를 기준으로 정렬하고 같을 경우 1번째 인자로 결정, 정렬에 있어 순위를 부여

et = 0
cnt = 0
for i in range(len(m)):
    if et <= m[i][0]:
        et = m[i][1]
        cnt+=1
print(cnt)

'''
tmp=[0] * m[len(m)-1][1]*2
res = 0
for j in range(n):
    cnt = 1
    tmp = [0] * m[len(m) - 1][1]*2
    for i in range(j, n):
        if 1 in tmp[m[i][0]:m[i][1]+1]:
            continue
        else:
            for k in range(m[i][0], m[i][1]+1):
                tmp[k]=1
        #if 1 not in tmp[m[i][0]:m[i][1]+1]:
        #if tmp[m[i][0]] == 0 and tmp[m[i][1]] == 0:
        #    for k in range(m[i][0], m[i][1]+1):
        #        tmp[k]=1
            #tmp[m[i][0]] = 1
            # ... 이 사이에 있는 것들도 다 1로 바꿔줘야 함.
            #tmp[m[i][1]] = 1
            #tmp[m[i][0]:m[i][1] + 1] = 1
            cnt += 1
    if cnt>=res:
        res = cnt

print(res)
'''