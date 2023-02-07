import sys
sys.stdin = open("input.txt", "rt")

import time
import math

# 1 2 3 4해서

# 순열 완전탐색
def dfs(v):
    st = time.time()
    global sum
    if v>=n:
        # 여기서 합을 구하기
        for i in range(1,n-1):
            sum+=ref[i]*arr[i]
            if sum>=m:
                sum=0
                return
        sum+=arr[0]+arr[n-1]
        if sum==m:
            for x in arr:
                print(x, end=" ")
            print()
            print("time : ", time.time()-st)
            sys.exit(0)
        sum=0
        return
    else:
        for i in range(1, n+1):
            if chk[i]==0:
                arr[v]=i
                chk[i]=1
                dfs(v+1)
                chk[i]=0

if __name__ == "__main__":
    start = time.time()
    n, m = map(int, input().split())
    sum=0
    chk = [0]*(n+1)
    arr = [0]*n
    ref = [1]*n
    for i in range(1, n-1):
        ref[i]=int(math.factorial(n-1)/(math.factorial(i)*math.factorial(n-1-i)))
    dfs(0)
    print("time : ", time.time()-start)