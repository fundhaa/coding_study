import sys
import time
sys.stdin = open("input.txt", "rt")

'''
def DFS(a, sum):
    # 각 노드의 값을 더해서 15가 될 때 a를 출력
    global cnt, tmp
    if sum>tot:
        cnt -=1
        sum -=a
        return
    elif sum==tot:
        if cnt<tmp:
            tmp=cnt
        cnt-=1
        sum-=a
        return
    else:
        for i in range(n):
            cnt+=1
            sum += a
            DFS(a+arr[i], sum)
'''
'''
def dfs(a):
    global sum,tmp, tmp2
    if sum==tot:
        if tmp>a:
            tmp=a
        sum-=tmp2
        return
    elif sum>tot:
        sum-=tmp2
        return
    else:
        for i in range(n):
            sum+=arr[i]
            tmp2=arr[i]
            print(sum)
            dfs(a+1)
'''
def dfs1(a, s):
    global tmp, tmp2
    if a>tmp:
        return
    if s==tot:
        if tmp>a:
            tmp=a
        s-=tmp2
        return
    elif s>tot:
        s-=tmp2
        return
    else:
        for i in range(n):
            tmp2=arr[i]
            dfs1(a+1,s+arr[i])
if __name__ == "__main__":
    start = time.time()
    n = int(input())
    arr = list(map(int, input().split()))
    #arr.sort(reverse=True)
    tot = int(input())
    cnt=0
    tmp=21470000
    tmp2 = 0
    sum=0
    #DFS(0,0)
    #dfs(0)
    dfs1(0,0)
    print(tmp)
    print("time :", time.time()-start)