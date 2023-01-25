import sys
sys.stdin = open("input.txt", "rt")

# list 사용
'''
str1 = input()
str2 = input()

ls1 = list(str1)
ls2 = list(str2)

for x in ls1:
    #print(x)
    if x in ls2:
        ls2.remove(x)

if not ls2:
    print("YES")
else:
    print("NO")
'''

a = input()
b = input()
str1 = dict()
for x in a:
    str1[x] = str1.get(x,0)+1 # x라는 key가 있었으면 x의 value 리턴하고 아님 0을 리턴
    # str1[x] = str1[x]+1 을 하면 안됨. 왜냐면 str1[x]가 정의가 안되어 있으면 keyerror가 남
for x in b:
    str1[x] = str1.get(x,0)-1

# 출력방법1
if any(val!=0 for key, val in str1.items()):
    print("NO")
else:
    print("YES")

# 출력방법2
for x in a:
    if str1.get(x)>0:
        print("NO")
        break
else:
    print("YES")