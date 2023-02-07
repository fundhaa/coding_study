import sys
sys.stdin = open("input.txt", "rt")

import time

def dfs(v):
    global cnt
    if v>=n-1:
        cnt+=1
        print(chk)
        return
    else:
        for j in range(n):
            if graph[v][j]==1:
                if chk[v]==0:
                    chk[v]=1
                    dfs(j)
                    chk[v]=0

if __name__ == "__main__":
    st = time.time()
    n, m = map(int, input().split())
    graph = [[0 for _ in range(n)] for _ in range(n)]
    rode = []
    for _ in range(m):
        rode.append(list(map(int, input().split())))

    for i in range(m):
        graph[rode[i][0]-1][rode[i][1]-1]=1
    cnt=0
    chk = [0]*n
    print(graph)
    dfs(0)
    print(cnt)

    print("time : ", time.time()-st)