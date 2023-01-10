import sys
sys.stdin=open("input.txt", "rt")

n = int(input())
arr=[]
if n>=2:
    arr.append(2)
for i in range(2, n+1):
    cnt = 0
    for j in range(2, i):
        if i%j != 0:
            cnt+=1
        if cnt==i-2:
            arr.append(i)
print(len(arr))
