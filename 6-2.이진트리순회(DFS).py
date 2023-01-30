import sys
sys.stdin = open("input.txt", "rt")

def DFS1(n): # 전위순회
    if n>7:
        return
    else:
        print(n, end=" ")
        DFS1(n*2)
        DFS1(n*2+1)

def DFS2(n): # 중위순회
    if n>7:
        return
    else:
        DFS2(n*2)
        print(n, end=" ")
        DFS2(n*2+1)

        # DFS1 > 37
        # 4251637

def DFS3(n): # 후위순회
    if n>7:
        return
    else:
        DFS3(n*2)
        DFS3(n*2+1)
        print(n, end=" ")
    # 4 5 26731


if __name__ == "__main__":
    DFS1(1)
    print()
    DFS2(1)
    print()
    DFS3(1)
