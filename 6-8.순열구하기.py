import sys
sys.stdin = open("input.txt", "rt")

import time

def dfs(a, b):
    if a>=m or a==b:
        print(arr)
        return
    else:
        for i in range(1, n+1):
            arr[a]=i
            dfs(a+1, i)

def DFS(v):
    global tmp
    global arr1
    if v>=m:
        print(arr)
        return
    else:
        for i in range(1,n+1):
            if arr1[i]==1:
                continue
            arr[v]=i
            arr1[i]=1
            DFS(v+1)
            arr1[i]=0

def dfss(node):
    global cnt
    if node>=m:
        for x in arr2:
            print(x, end= " ")
        print()
        cnt+=1
        return
    else:
        for i in range(1, n+1):
            if chk[i]==0:
                arr2[node]=i
                chk[i] = 1
                dfss(node+1)
                chk[i]=0




if __name__ == "__main__":
    start = time.time()
    n, m = map(int, input().split())
    arr = [0]*m
    arr1 = [0]*(n+1)
    arr2 = [0]*m
    chk = [0]*(n+1)
    cnt=0
    dfs(0, -1)
    print()
    tmp=0
    DFS(0)
    print()
    dfss(0)
    print(cnt)

    print("time : ", time.time()-start)




