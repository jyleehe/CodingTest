# https://programmers.co.kr/learn/courses/18/lessons/1882
#

def dfs(strs, remain, res):
    # global anslist
    if remain == '':
        return res

    for chunk in strs:
        idx = remain.find(chunk)
        if idx != -1:
            # print(chunk)
            res = max(dfs(strs, remain[:idx], res + 1), dfs(strs, remain[idx + len(chunk):], res + 1))
            # print(res)
            anslist.append(res)
            # if res == 2:
            #     return 1

    return 0


def solution(strs, t):
    global anslist
    ans = 0
    anslist = []

    sorted_strs = sorted(strs, key=lambda x: len(x), reverse=True)
    print(sorted_strs)
    ans = dfs(sorted_strs, t, 0)
    print(anslist)

    # pseudo code
    # 1. find max len string chunk in t
    # they are candidates
    # for each candidates, do:
    # split t into left and right
    # find max len string in left and right
    # until complete
    # only pass when both left and right are completed
    # otherwise -1
    # return min([result_candidates > 0]) if max(result_candidates) > -1
    # if max(result) == -1
    # go to 1. and maxlen -= 1

    return ans