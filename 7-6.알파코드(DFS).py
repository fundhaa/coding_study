import sys

sys.stdin = open("input.txt", "rt")

import time

def dfs(L, v):
    global res
    global cnt
    if L>=l:
        cnt+=1
        for i in range(len(v)):
            print(chr(v[i]+64),end="")
        print()
        return

    else:
        for i in range(1, 26):
            if arr[L]==i:
                res.append(arr[L])
                dfs(L+1, res)
                res.pop()
            if L<l-1:
                if str(arr[L])+str(arr[L+1])==str(i):
                    res.append(int(str(arr[L])+str(arr[L+1])))
                    dfs(L+2, res)
                    res.pop()


if __name__ == "__main__":
    st = time.time()
    n = input()
    l = len(n)
    arr = list()
    for i in range(len(n)):
        arr.append(int(n[i]))
    res = list()
    cnt=0
    dfs(0,res)
    print(cnt)







    print("time : ", time.time() - st)