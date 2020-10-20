# https://programmers.co.kr/learn/courses/18/lessons/1882
#
# BFS 로 풀어보려 했는데 실패함..
# 단어가 완성됐을 때 word 사용 횟수는 카운트 가능.
# 여러 단어 후보들에 대해서도 탐색하고 있음.
# 문제는, 완성할 수 없는 경우를 고려하지 않고 전부 cnt 하고 있음.
# 끝까지 제대로 갔는지를 확인해야 되기 때문에, DFS 로 풀어야 할거 같음.
# 아니면 BFS + DFS 로 해야되나?

def search(strs, target_list):
    # BFS
    # this is like q.pop()
    while target_list:
        target, cnt, res = target_list.pop(0)
        # print(target, cnt)
        # print(target_list[0], target_list[1])
        # append left and right
        for chunk in strs:  # search words from longest to shortest
            idx = target.find(chunk)
            if idx != -1:  # if there is word!
                left = target[:idx]
                right = target[idx + len(chunk):]
                # print("left:", left)
                # print("right:", right)
                if left != '':
                    target_list.append((left, cnt + 1, chunk + res))
                if right != '':
                    target_list.append((right, cnt + 1, res + chunk))
    if idx == -1:  # if there isn't
        return -1

    return cnt


def solution(strs, t):
    global anslist
    ans = 0
    anslist = []

    sorted_strs = sorted(strs, key=lambda x: len(x), reverse=True)
    # print(sorted_strs)
    ans = search(sorted_strs, [(t, 0)])
    # print(anslist)

    # pseudo code
    # 1. find max len string chunk in t
    # they are candidates
    # for each candidates, do:
    # split t into left and right
    # find max len string in left and right
    # until complete
    # only pass when both left and right are completed
    # otherwise -1
    # return min([cntult_candidates > 0]) if max(cntult_candidates) > -1
    # if max(cntult) == -1
    # go to 1. and maxlen -= 1

    return ans