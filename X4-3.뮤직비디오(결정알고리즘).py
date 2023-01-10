import sys
sys.stdin = open("input.txt", "rt")

def Count(capacity):
    # DVD 용량을 리턴해줌
    cnt = 1
    sum = 0
    for x in arr:
        if sum+x>capacity and mid>=max(arr): # 가장 긴 노래를 담을 수 있는 길이여야 함.
            cnt+=1
            sum=x
        else:
            sum+=x
    return cnt

n, m = map(int, input().split())
arr = list(map(int, input().split()))

# 9개 곡, 3개의 DVD
# DVD의 최소 용량은?
# DVD 용량을 이분검색 해야함.

ldx = min(arr)
rdx = sum(arr)
res = 0
while ldx <= rdx:
    mid=(ldx+rdx)//2
    if Count(mid)<=m:
        res = mid
        rdx = mid-1
    else:
        ldx=mid+1
print(res)
