import sys
sys.stdin=open("input.txt","rt")

import time

def dfs(L, T, P):
    global ans
    if T>n:
        return
    if T==n:
        if P>ans:
            ans = P
        return
    else:
        for i in range(T, n):
            dfs(L+1, i+arr[i][0], P+arr[i][1])
            #dfs(L+1, T+1, P)
            # 1일 수행
            # dfs 4, 20
            # dfs 6+i, 50
            # 1일은 안하고 2일부터 한다치면
            # dfs 2, 10
            # 3일 부터
            # dfs 3, 15 시작 날짜를 더해줘야함
            #dfs(L+1, T+1, P)

#현재위치에 대한걸 넣어줘야함.
# def ( 현재 날짜, 소득,

if __name__=="__main__":
    st = time.time()
    n=int(input())
    arr=list()
    for _ in range(n):
        arr.append(list(map(int,input().split())))
    ans=0
    dfs(0,0,0)
    print(ans)


    print("time : ", time.time()-st)