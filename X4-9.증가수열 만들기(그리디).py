import sys
sys.stdin = open("input.txt", "rt")

n = int(input())
m = list(map(int, input().split()))
str = ""
cnt=0
tmp=-1
lt = 0
rt = n-1
arr=[]
while lt<rt:
    if tmp<m[lt] and m[lt]<m[rt]:
        str += "L"
        cnt += 1
        tmp = m[lt]
        arr.append(tmp)
        lt += 1

    elif m[lt]<tmp and tmp<m[rt]:
        str += "R"
        cnt += 1
        tmp = m[rt]
        arr.append(tmp)
        rt -= 1

    elif m[lt]<m[rt] and m[rt]<tmp:
        break

    elif tmp<m[rt] and m[rt]<m[lt]:
        str += "R"
        cnt += 1
        tmp = m[rt]
        arr.append(tmp)
        rt -= 1

    elif m[rt]<tmp and tmp<m[lt]:
        str += "L"
        cnt += 1
        tmp = m[lt]
        arr.append(tmp)
        lt += 1

    elif m[rt]<m[lt] and m[lt]<tmp:
        break


print(cnt)
print(str)
