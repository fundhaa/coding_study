import sys
sys.stdin=open("input.txt", "rt")
m = [list(map(int, input().split())) for i in range(9)]


dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [-1, -1, -1, 0, 0, 1, 1, 1]

cnt=0
for i in range(1, 9, 3):
    for j in range(1, 9, 3):
        if all(m[i][j]!=m[i+dx[k]][j+dy[k]] for k in range(8)):
            cnt+=1

ref = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]

for i in range(9):
    for j in range(9):
        if m[i][j] in ref:
            ref.remove(m[i][j])
        if m[j][i] in ref:
            ref.remove(m[j][i])
    if ref == []:
        ref = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]
    else:
        for k in range(1, 10):
            ref.append(k)
            ref.append(k)


'''
for i in range(9):
    if all(m[i][j]!=m[i][j+1] for j in range(8)):
        cnt+=1
    if all(m[h][i]!=m[h+1][i] for h in range(8)):
        cnt+=1
'''
if ref == [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9] and cnt==9:
    print("YES")
else:
    print("NO")