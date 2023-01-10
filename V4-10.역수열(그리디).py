import sys
sys.stdin = open("input.txt", "rt")

n = int(input())
m = list(map(int, input().split()))

arr = [0]*(n)
for i in range(n): # 원 수열 고정용
    idx=0
    for j in range(n): # 답 수열 0 탐색용
        if idx==m[i]:
            if arr[j] == 0:
                arr[j]=i+1
                break

        elif idx<m[i]:
            if arr[j] == 0:
                idx+=1

for x in arr:
    print(x, end= " ")