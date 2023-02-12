import sys

sys.stdin = open("input.txt", "rt")

import time
# 1 2 6
# 1
# 2
# 3
# 4 // 2담고 옆에 6하면
# 5 // 1담고 옆에 6
# 6
# 7 // 6 1
# 8 // 6 2
# 9 // 6 2 1

# 1 5 7

# dfs
# 트리를 그리면 더하고 빼고 하되. 1보다는 커야 함.
# max 는 sum

def dfs(v, s):
    global tot
    global chk
    if v>=n:
        if s<=0 and s>tot:
            return
        else:
            chk[s]=1
            return
    else:
         # 왜 s 에 arr[i]가 안더해지지?
         # 왜 s 가 계속 0이지?
        for i in range(n):
            if s>=0 and s<=tot:
                if nchk[arr[i]]==1:
                    continue
                else:
                    nchk[arr[i]]=1
                    dfs(v+1, s+arr[i])
                    nchk[arr[i]] = 0
                    nchk[arr[i]] = 1
                    dfs(v+1, s) # 더하지 않는 경우도 체크
                    nchk[arr[i]]=0
                    nchk[arr[i]]=1
                    dfs(v+1, s-arr[i])
                    nchk[arr[i]]=0

# set 이라는 자료구조 : 중복을 피하면서 요소 추가 가능.



def dfs1(v, s):
    global tot
    global chk
    # 전체 결과 값 ( +-1 +-3 +-4 +-5 +-7 +-8 )
    # 지금까지 더한 결과 값 s 이건 음수일 수 있음
    # 양수로 취급하고 다 더한 값 tot
    # tot 에서 s(음수)를 더하고 그럼 안더한 숫자들을 다 플러스로 취급하고 더한 값
    # 이게 음수면 return.
    # 안더한 숫자들은 tot + s
    #if s>0 and chk[tot-s]

    if s<0:
        if tot+(2*s)<0:
            return

    if s>0 and tot-s>0:
        chk[s]=1
        #chk[tot-s]=1
    if v>=n:
        if s>0 and s<=tot:
            chk[s]=1
            return
        else:
            return
        #print(v, s)
    else:
        # 더하거나 그대로거나 빼거나
        # 근데 똑같은걸 여러번 더하면 안되니까
        # 체크리스트를 활용
        for i in range(n):
            if cl[i]==0:
                cl[i]=1
                dfs1(v+1, s+arr[i])
                dfs1(v+1, s-arr[i])
                cl[i]=0

def dfs2(L,s):
    if L>=n:
        if s>0 and s<=tot:
            res.add(s)
    else:
        dfs2(L+1, s+arr[L])
        dfs2(L+1, s-arr[L])
        dfs2(L+1, s)


if __name__ == "__main__":
    st = time.time()
    n = int(input())
    arr = list(map(int,input().split()))
    tot = sum(arr)
    chk = [0]*(tot+1)
    cl = [0]*(n)
    nchk = [0]*(max(arr)+1)
    res=set()
    #여기서 chk value가 0인 index 출력
    #dfs1(0,0)
    cnt=0
    for x in arr:
        chk[x]=1
    for i in range(1, len(chk)):
        if chk[i]==0:
            cnt+=1
    #print(arr)
    #print(cnt)
    #print(chk)
    dfs2(0,0)
    print(tot-len(res))
    print("time : ", time.time() - st)