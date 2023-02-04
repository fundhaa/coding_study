import sys
sys.stdin = open("input.txt", "rt")

def DFS(a, b):
    global n
    global m
    global cnt
    if a>=n or b>=m:
        cnt+=1
        print(arr)
        return
    else:
        for i in range(1, n+1):
            arr[b]=i
            DFS(a+1, b+1)

# 0, 1, 2 는 트리의 레벨
# 각 레벨당 총 n 개의 노드가 있다.
#

if __name__ == "__main__":
    n, m =map(int, input().split())
    cnt=0
    arr=[0]*m
    DFS(0,0)
    print(cnt)