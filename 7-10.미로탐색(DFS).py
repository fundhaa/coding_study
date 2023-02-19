import sys
sys.stdin = open("input.txt", "rt")

def dfs(x, y):
    global cnt
    if x==6 and y==6:
        cnt+=1
        return
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<=6 and 0<=ny<=6:
                if chk[nx][ny]==0 and arr[nx][ny]==0:
                    chk[nx][ny]=1
                    dfs(nx,ny)
                    chk[nx][ny]=0

if __name__ == "__main__":
    arr=list()
    for _ in range(7):
        arr.append(list(map(int, input().split())))
    cnt=0
    chk=[[0]*7 for _ in range(7)]
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    chk[0][0]=1
    dfs(0,0)
    print(cnt)