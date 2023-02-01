import sys
sys.stdin = open("input.txt", "rt")

def DFS(a):
    global cnt
    global m
    global n
    if a>=m:
        print(arr)
        cnt+=1
        return
    else:
        for i in range(1,n+1):
            arr[a]=i
            DFS(a+1)

if __name__ == "__main__":
    n, m = map(int, input().split())
    cnt = 0
    arr=[0]*(m)
    DFS(0)
    print(cnt)