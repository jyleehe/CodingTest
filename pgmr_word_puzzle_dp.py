# 해설 참조 후 DP 로 해결:
# https://m.blog.naver.com/PostView.nhn?blogId=meeting0103&logNo=221091812181&proxyReferer=https:%2F%2Fwww.google.com%2F

def solution(strs, t):
    ans = 0
    cnt = len(strs)

    dp = [0] * (len(t) + 1)  # init dp + len(t), idx starts with 1
    dp[0] = len(strs) + 1  # initial minimum count = # of all candidates + 1
    # print(dp)

    for idx, digit in enumerate(t, 1):
        subs = t[:idx]
        # dp
        cnts = []
        # find minimum counts to make substring until this digit
        for cand in strs:
            candlen = len(cand)
            # print(candlen)
            if candlen <= len(subs) and cand == subs[-candlen:]:
                # print("dp")
                if cand == subs:
                    cnts.append(1)
                else:
                    cnts.append(dp[idx - candlen] + 1)
            # print(cnts)
            if cnts:
                dp[idx] = min(cnts)
        # break
    if dp[-1] == 0:
        return -1
    else:
        return dp[-1]