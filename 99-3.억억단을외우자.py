def solution(e, starts):
    # 시간초과;;;
    # 힙을 써야하나
    ans = []
    tmp = []
    for i in range(len(starts)):
        cnt = 0
        ans.append(cnt)
        tmp.append(cnt)
        for j in range(starts[i], e + 1):
            for k in range(1, j + 1):
                if j % k == 0:
                    cnt += 1
            if cnt > ans[i]:
                ans[i] = cnt
                tmp[i] = j

            cnt = 0
            # j가 어떤 수들의 곱으로 이루어지는지를 확인해야 함.
            # 이거는 starts[i] 부터 e+1까지 하나씩 올려가면서 나눠 떨어지는지 보고 나눠떨어지면 +1씩 더하면 되겠다.
            # 그리고 그 어떤 수들의 조합이 몇개인지 저장.
            # 갯수가 저장된 값보다 크면 갱신 같으면 무시
            # 배열에 저장해서 배열을 출력하면 됨.
            # 각 라운드별로 저장하는 위치는 ans[i] 이면 됨.

    return tmp