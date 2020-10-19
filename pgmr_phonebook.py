# https://programmers.co.kr/learn/courses/30/lessons/42577#
# 효율성 문제


from collections import defaultdict


def solution(phone_book):
    answer = True
    idict = defaultdict(list)
    phone_book = sorted(phone_book)
    for i, p in enumerate(phone_book):
        for k in idict.keys():
            if len(p) >= k:
                idict[k].append((i, p[:k]))
        if (i, p) not in idict[len(p)]:
            idict[len(p)].append((i, p))
            # print(idict)

    for i, p in enumerate(phone_book):
        for (idx, val) in idict[len(p)]:
            if idx != i and p == val:
                answer = False

    return answer