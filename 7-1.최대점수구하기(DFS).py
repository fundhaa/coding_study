import sys
sys.stdin = open("input.txt", "rt")

import time


def dfs(grade, time):
    global ans
    global tottime
    if time>m:
        if all(chk[i]==1 for i in range(n)):
            sys.exit(0)
        return
    else:
        for i in range(n):
            if chk[i]==0 and tottime-arr[i][1]>0:
                grade += arr[i][0]
                time += arr[i][1]
                tottime-=arr[i][1]
                chk[i]=1
                if time<=m and grade>ans:
                    ans=grade
                dfs(grade, time)
                grade -= arr[i][0]
                time -= arr[i][1]
                tottime+=arr[i][1]
                chk[i]=0

def advanced_dfs(L, grade, time):
    global ans
    if time>m:
        return
    if L>=n:
        if grade>ans:
            ans = grade
        return
    else:
        advanced_dfs(L+1, grade+arr[L][0], time+arr[L][1])
        advanced_dfs(L+1, grade, time)

if __name__ == "__main__":
    st = time.time()
    n, m = map(int, input().split())
    arr = []
    chk = [0]*n
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    ans = 0
    t = 0
    tottime=0
    for i in range(n):
        tottime +=arr[i][1]
    #dfs(0, 0)
    ans=0
    advanced_dfs(0,0,0)
    print(ans)



    print("time : ", time.time()-st)