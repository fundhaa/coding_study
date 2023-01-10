import sys
sys.stdin = open("input.txt", "rt")
# 이건 정렬해서 순서대로 더해서 풀 문제가 아니다.
# 가장 무거운 사람과 가벼운 사람을 조합해서 최소 보트 개수를 구해야함.
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
cnt=0
while len(arr)!=0:
    if len(arr)==1:
        cnt+=1
        break
    if arr[-1]+arr[0]<=m:
        arr.pop()
        arr.pop(0)
        cnt+=1
    else:
        arr.pop()
        cnt+=1

print(cnt)
