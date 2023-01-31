import sys
sys.stdin = open("input.txt", "rt")

def DFS(v, sum):
    global res # main 함수의 res 가져오기
    if sum>c:
        return
    else:
        if sum>ans[0]:
            ans[0]=sum
            res=sum
    if v>=n:
        return
    else:
        DFS(v + 1, sum)
        DFS(v+1, sum+arr[v])

if __name__ == "__main__":
    c, n = map(int, input().split())
    arr = []
    ans=[0]
    res = 0
    for _ in range(n):
        arr.append(int(input()))
    DFS(0, 0)
    print(ans[0])
    print(res)
