import sys
sys.stdin = open("input.txt", "rt")

import time

def dfs(v, s):
    global cnt
    if v>=k:
        if sum(res)%m==0:
            cnt+=1

    else:
        for i in range(s, n+1):
            if i<v:
                continue
            if chk[i]==0:
                res[v]=arr[i-1]
                chk[i]=1
                dfs(v+1, i+1)
                chk[i]=0


if __name__ == "__main__":
    st = time.time()
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    m = int(input())
    chk = [0]*(n+1)
    res = [0]*k
    cnt=0
    dfs(0, 1)
    print(cnt)


    print("time: ", time.time()-st)