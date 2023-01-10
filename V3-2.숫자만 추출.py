import sys
sys.stdin = open("input.txt", "rt")

def yaksu(x):
    cnt=0
    for i in range(1, x+1):
        if x%i==0:
            cnt += 1
    return cnt

str = list(input())
ans="0"
for i in range(len(str)):
    if ord(str[i]) >=48 and ord(str[i]) <=57:
        ans += str[i]
print(int(ans))
print(yaksu(int(ans)))

# 강사 풀이
'''
str = input()
for x in s:
    if x.isdecimal():
        res = res*10+int(x)
print(x)
'''