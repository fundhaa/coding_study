import sys
sys.stdin = open("input.txt", "rt")

import time

def dfs(v):
    global chk
    if v>=m:
        for x in arr:
            print(x, end =" ")
        print()
        return
    else:
        for i in range(1, n+1):
            if chk[i]==0:
                arr[v]=i
                chk[i]=1
                dfs(v+1)
                if v!=0:
                    chk[i]=0

if __name__ == "__main__":
    st = time.time()
    n, m = map(int, input().split())
    arr = [0]*m
    chk = [0]*(n+1)

    dfs(0)

    print("time : ", time.time()-st)