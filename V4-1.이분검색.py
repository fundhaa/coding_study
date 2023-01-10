import sys
sys.stdin = open("input.txt", "rt")
n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
res = arr.index(m)
print(res+1)

# 맞긴 맞았는데 이분검색으로 푼건 아니다
# 이분 검색이란 가운데 index를 찾고 그것보다 작은가? 큰가? 비교해서 범위를 점점 좁혀나가는 것.

lt = 0
rt = len(arr)-1

while(lt<=rt):
    mid = (lt + rt) // 2
    if arr[mid]==m:
        print(mid+1)
        break
    elif arr[mid]>m:
        rt=mid-1
    else:
        lt=mid+1