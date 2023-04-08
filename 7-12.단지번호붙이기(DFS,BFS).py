import sys
import time
sys.stdin = open("input.txt", "rt")

def dfs(st):
    global num
    for i in range(4):
        x = dx[i]+st[0]
        y = dy[i]+st[1]
        new = (x,y)
        if 0<=x<n and 0<=y<n and chk[x][y]==0 and arr[x][y]==1:
            chk[x][y]=1
            num+=1
            dfs(new)

if __name__ == "__main__":
    stt = time.time()
    n = int(input())
    arr = list()
    for _ in range(n):
        arr.append(list(map(int, input().strip())))
    chk = [[0 for _ in range(n)] for _ in range(n)]
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    st=(0, 0)
    cnt=0
    num=0
    ans = list()
    checker=1
    for i in range(n):
        for j in range(n):
            if arr[i][j]==1 and chk[i][j]==0:
                st = (i,j)
                cnt+=1
                dfs(st)
                if num==0:
                    num=1
                ans.append(num)
                num=0
    print(cnt)
    ans.sort()
    for x in ans:
        print(x)
    print(time.time()-stt)
