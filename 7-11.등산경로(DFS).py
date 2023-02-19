import sys
sys.stdin = open("input.txt", "rt")

import time

def dfs(x, y):
    global cnt
    if x == mxix[0] and y == mxix[1]:
        cnt+=1
        return
    else:
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<=n-1 and 0<=ny<=n-1:
                if chk[nx][ny]==0 and arr[x][y]<arr[nx][ny]:
                    chk[nx][ny]=1
                    dfs(nx, ny)
                    chk[nx][ny]=0

if __name__ == "__main__":
    st = time.time()
    n = int(input())
    arr = list()
    for i in range(n):
        arr.append(list(map(int, input().split())))
    chk = [[0]*n for _ in range(n)]
    # 최솟값 index, 최댓값 index 찾기
    mn = min(map(min, arr))
    mx = max(map(max, arr))
    mnix = mxix = (0,0)
    for i in range(n):
        if arr[mnix[0]][mnix[1]] == mn and arr[mxix[0]][mxix[1]]==mx:
            break
        for j in range(n):
            if mx == arr[i][j]:
                mxix = (i, j)
                continue
            if mn == arr[i][j]:
                mnix = (i, j)
                continue
    # 상하좌우 계산
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    cnt=0
    chk[mnix[0]][mnix[1]]=1
    dfs(mnix[0], mnix[1])
    print(cnt)



    print(time.time()-st)