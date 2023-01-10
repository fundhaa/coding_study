import sys
sys.stdin=open("input.txt","rt")
m = [list(map(int, input().split())) for _ in range(7)]
cnt=0
for i in range(7):
    for j in range(3):
        if m[i][j]==m[i][j+4] and m[i][j+1]==m[i][j+3]:
            cnt+=1

        if m[j][i]==m[j+4][i] and m[j+1][i]==m[j+3][i]:
            cnt +=1

print(cnt)

# 회문탐색
for i in range(3):
    for j in range(7):
        tmp = m[j][i:i+5]
        if tmp==tmp[::-1]: # 이거 배열 뒤집는 것. 회문 비교할때 많이 쓴다.
            cnt+=1