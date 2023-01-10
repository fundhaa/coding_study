import sys
sys.stdin=open("input.txt", "rt")
n, k = map(int, input().split())
arr = list(map(int, input().split()))
# set : 중복을 취급 안하는 자료구조
res = set()
for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1,n):
            res.add(arr[i]+arr[j]+arr[m]) # set 은 add 로 인자를 추가한다.
res = list(res) # set은 sort가 안되기 때문에 list화 시켜주어야 한다.
res.sort(reverse=True) # 내림차순으로 정렬
print(res[k-1])
