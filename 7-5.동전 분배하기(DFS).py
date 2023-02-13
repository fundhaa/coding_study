import sys

sys.stdin = open("input.txt", "rt")

import time

def dfs(L, v):
    global ans
    global tmp
    if L>=n:
        ss = set(v)
        if len(ss)==3:
            if max(v)-min(v)<ans:
                ans = max(v)-min(v)

    else:
        for i in range(3):
            v[i]=v[i]+arr[L]
            dfs(L+1, v)
            v[i]=v[i]-arr[L]

if __name__ == "__main__":
    st = time.time()
    n = int(input())
    arr = list()
    for _ in range(n):
        arr.append(int(input()))

    tmp = [0, 0, 0]
    chk = [0]*n
    ans = 21470000
    dfs(0, tmp)
    print(ans)
    print("time : ", time.time() - st)