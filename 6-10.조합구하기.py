import sys
sys.stdin = open("input.txt", "rt")

import time

def dfs(v, s):
    global chk
    if v>=m:
        for x in arr:
            print(x, end =" ")
        print()
        return
    else:
        for i in range(s, n+1):
            if chk[i]==0:
                arr[v]=i
                chk[i]=1
                dfs(v+1, i+1)
                #if v!=0:
                chk[i]=0

# 최적의 조합 산출 코드(코드길이가 짧음)
def dfs2(v, s):
    if v>=m:
        print(arr1)
        return
    else:
        for i in range(s,n+1):
            arr1[v] = i
            dfs2(v+1, i+1)

if __name__ == "__main__":
    st = time.time()
    n, m = map(int, input().split())
    arr = [0]*m
    chk = [0]*(n+1)
    arr1 = [0]*m

    dfs(0,1)
    dfs2(0, 1)

    print("time : ", time.time()-st)