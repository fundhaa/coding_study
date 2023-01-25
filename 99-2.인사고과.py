def solution(scores):
    # scores[0] 등수

    # 일단 인센티브를 받을 수 있는지 없는지
    # 인센티브를 못받는 경우 리스트에서 제외
    '''
    a = dict()
    i=1
    for x in scores:
        a[i]=x[0]+x[1]
        i+=1
    print(a)
'''
    for x in scores:
        i = 0
        while True:
            if i >= len(scores) - 1:
                break
            if x[0] < scores[i][0] and x[1] < scores[i][1]:
                if x[0] == scores[0][0] and x[1] == scores[0][1]:
                    return -1
                scores.remove(x)
                break
            i += 1

    # 그리고 순차적으로 정렬
    ans = []
    for x in scores:
        ans.append(x[0] + x[1])

    tmp = ans[0]
    ans.sort(reverse=True)
    answer = ans.index(tmp) + 1
    print(answer)
    return answer