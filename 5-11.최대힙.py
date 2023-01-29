import sys
import heapq as hq
sys.stdin = open("input.txt", "rt")

ans = []
while True:
    n = int(input())
    if n == -1:
        break
    elif n == 0:
        if len(ans)==0:
            print(-1)
        else:
            print(-hq.heappop(ans))
    else:
        hq.heappush(ans, -n)