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

if __name__ == "__main__":
    n = int(input())
    ans = ""
    dv(n, ans)

