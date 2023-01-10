import sys
sys.stdin=open("input.txt", "rt")
n = int(input())
arr = list(map(int, input().split()))

def reverses(x):
    arr = []
    tmp="0"
    for i in str(x):
        arr.append(i)
    for i in range(len(arr)-1, -1, -1):
        tmp+=arr[i]
    return int(tmp)

def isPrime(x):
    arr=[]
    if x==1:
        return 0
    for i in range(2, x):
        if x%i == 0:
            arr.append(i)
    if len(arr)==0:
        return x
    else:
        return 0
res=[]
for i in range(n):
    tmp = reverses(arr[i])
    tmp = isPrime(tmp)
    if tmp != 0:
        res.append(tmp)

for i in range(len(res)):
    print(res[i], end= " ")
