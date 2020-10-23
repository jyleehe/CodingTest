# 해설 참조 후 DP 로 해결:
# https://m.blog.naver.com/PostView.nhn?blogId=meeting0103&logNo=221091812181&proxyReferer=https:%2F%2Fwww.google.com%2F

def solution(strs, t):
    ans = 0
    cnt = len(strs)

    dp = [0] * (len(t) + 1)  # init dp + len(t), idx starts with 1
    dp[0] = len(strs) + 1  # initial minimum count = # of all candidates + 1
    print(dp)

    for idx, digit in enumerate(t, 1):
        print(idx, digit)
        # find minimum counts to make substring until this digit
        subs = t[:idx]
        # dp
        for cand in strs:
            candlen = len(cand)
            if candlen <= len(subs) and cand == subs[-candlen:]:
                print("dp")
                dp[idx] = min(dp[idx - candlen] + 1, cnt)

    return ans