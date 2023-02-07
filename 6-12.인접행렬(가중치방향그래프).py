import sys
sys.stdin = open("input.txt", "rt")

import time


if __name__ == "__main__":
    st = time.time()
    n, m = map(int, input().split())
    arr = []
    for i in range(m):
        arr.append(list(map(int, input().split())))
    print(arr)
    ans = [[0 for _ in range(n)] for _ in range(n)]
    print(ans)
    for i in range(m):
        ans[arr[i][0]-1][arr[i][1]-1]=arr[i][2]
    for x in ans:
        for a in x:
            print(a, end=" ")
        print()




    print("time : ", time.time()-st)