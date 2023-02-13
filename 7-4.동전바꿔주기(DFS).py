import sys

sys.stdin = open("input.txt", "rt")

import time

def dfs(L, v):
    global cnt
    global n
    if v>T:
        return
    if L==k:
        if v==T:
            cnt+=1
        return

    else:
        for i in range(n[L]+1):
            dfs(L+1, v+p[L]*i)


if __name__ == "__main__":
    st = time.time()
    # 입력을 받는 부분
    T = int(input()) # 지폐의 금액
    k = int(input()) # 동전의 가짓수
    p = list() # 동전의 금액
    n = list() # 동전의 갯수
    for i in range(k):
        a, b = map(int, input().split())
        p.append(a)
        n.append(b)

    # 합수 실행 부분
    cnt=0
    dfs(0, 0)
    print(cnt)


    print("time : ", time.time() - st)