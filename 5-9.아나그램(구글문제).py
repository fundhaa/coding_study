import sys
sys.stdin = open("input.txt", "rt")

from collections import deque

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