# https://programmers.co.kr/learn/courses/30/lessons/42577#
# 효율성 문제에서 걸림.
# dict 만들어서 했는데, 다른 방식으로 풀어봐야 할 듯.

# 다른 사람 코드
def solution(pb):
    answer = True
    dic = {}
    for p in pb:
        dic[p] = 1

    for p in pb:
        tmp = ''
        for num in p:
            tmp += num
            if tmp in dic and tmp != p:
                answer = False

    return answer
#
#
# from collections import defaultdict
#
#
# def solution(phone_book):
#     answer = True
#     idict = defaultdict(list)
#     phone_book = sorted(phone_book) # for test case "0010111" - leading zeros
#
#     for i, p in enumerate(phone_book):
#         for k in idict.keys():
#             if len(p) >= k:
#                 idict[k].append((i, p[:k]))
#         if (i, p) not in idict[len(p)]:
#             idict[len(p)].append((i, p))
#             # print(idict)
#
#     for i, p in enumerate(phone_book):
#         for (idx, val) in idict[len(p)]:
#             if idx != i and p == val:
#                 answer = False
#
#     return answer