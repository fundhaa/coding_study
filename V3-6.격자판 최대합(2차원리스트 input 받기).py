import sys
sys.stdin=open("input.txt", "rt")
n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]
large=0
sum_col = sum_row = sum_zig = sum_zag = 0

for i in range(n):
    tmp1=tmp2=0
    for j in range(n):
        tmp1+=m[i][j] #sum_row
        tmp2+=m[j][i] #sum_col
    if sum_row < tmp1:
        sum_row=tmp1
    if sum_col < tmp2:
        sum_col=tmp2
    sum_zig += m[i][i]
    sum_zag += m[i][n - i - 1]
print(max(sum_col, sum_zag, sum_row, sum_zig))