import sys
sys.stdin=open("input.txt", "rt")

n = int(input())
arr = list(map(int, input().split()))
avg = round(sum(arr)/n) # round : 소수점 첫째자리에서 반올림인데 round half even 방식을 따른다.
avgMin=float('inf')
for idx, x in enumerate(arr):
    tmp= abs(x-avg)
    if tmp<avgMin:
        avgMin=tmp
        score = x
        res = idx+1

    elif tmp==avgMin:
        if x>score:
            score = x
            res = idx+1
print("%d %d" %(avg, res))




'''
#print(avg)
avgMin=float('inf')

for i in range(n):
    if arr[i]-avg<arrMin:
        if arr[i]-avg<0:
            midx=i
            arrMin = avg-arr[i]
        else:
            idx = i
            arrMin = arr[i]-avg

if arr[idx]>arr[midx]:
    print(arr[idx])
elif arr[idx]==arr[midx]:
    if idx>midx:
        print(arr[midx])
    else:
        print(arr[idx])
'''