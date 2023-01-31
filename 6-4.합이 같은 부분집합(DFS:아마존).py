import sys
sys.stdin = open("input.txt", "rt")

def DFS(L, sum):
    if sum>tot//2:
        return
    if L>=n:
        if sum == tot-sum:
            print("YES")
            sys.exit(0) # 아예 이 파이썬 프로그램 종료
    else:
        DFS(L+1,sum+arr[L])
        DFS(L+1,sum)


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    tot = sum(arr)
    DFS(0, 0) # YES 가 출력되면 프로그램이 종료되어 다음 문장 실행 X
    print("NO") # 이 라인까지 왔다는건 DFS 함수에서 YES가 안나왓단소리
