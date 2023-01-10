import sys
sys.stdin = open("input.txt", "rt")

n = int(input())
arr = list(map(int, input().split()))

def digit_sum(x):
    sum=0
    while x>0:
        sum+=x%10
        x=x//10
    return sum

def digit_sum2(x):
    sum = 0
    for i in str(x):
        sum+=int(i)
    return sum

max = 0
for x in arr:
    tot = digit_sum(x)
    if tot>max:
        max = tot
        res = x
print(res)

