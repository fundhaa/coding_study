import sys
sys.stdin = open("input.txt", "rt")

def dv(a, ans):
    if a>0:
        ans += str(a % 2)
        a = a//2
        dv(a, ans)
    else:
        ans = ans[::-1]
        print(ans)

def DFS(x):
    if x<=0:
        return
    else:
        DFS(x//2)
        print(x%2, end="")

if __name__ == "__main__":
    n = int(input())
    ans = ""
    dv(n, ans)
    DFS(n)

