import sys
sys.stdin=open("input.txt", "rt")
n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]
sum = 0

s = e = n//2
f=0
for i in range(0,n):
    for j in range(s,e+1):
        sum+=m[i][j]
    if i<n//2:
        s-=1
        e+=1
    else:
        s+=1
        e-=1
    if s==0:
        f=1
print(sum)
'''
for i in range(0,n):
    if i>n//2:
        for j in range(0, n-i):
            print(m[i][2*(n-1)-2*i+1])
    else:
        for j in range(0, i):
            print(m[i][2*i-1])
            '''
'''

for i in range(0, n):
    if i>n//2:
        i = n-i
    for j in range(0, i):
        sum+=m[i][j]
print(sum)
sum+=m[0][n//2]
sum+=m[n//2][0]
sum+=m[n//2][n-1]
sum+=m[n-1][n//2]

print(sum)

12345


        1,3
    2,2 2,3 2,4
3,1 3,2 3,3 3,4 3,5

for i in range(1, 10):
    if i > 5:
        i = 10 - i
    for j in range(0, i):
        print("*", end = "")
    print()


for i in range(1, 12):
    if i>6:
        print("#"*(i-6)+"*"*(23-2*i))
    else:
        print("#"*(6-i)+"*"*(2*i-1))
'''