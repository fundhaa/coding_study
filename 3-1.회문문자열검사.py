import sys
sys.stdin = open("input.txt", "rt")

n = int(input())
for i in range(n):
    str = list(input().upper())
    rev_str = str[::-1]
    cnt = 0
    for j in range(len(str)//2):
        if str[j] == str[-j-1]:
            cnt+=1
    if cnt==len(str)//2:
        print("#%d YES" %(i+1))
    else:
        print("#%d NO" %(i+1))
