def solution(triangle):
    answer = 0
    dp = [[0] * (t + 1) for t in range(len(triangle))]
    # print(dp)
    dp[0] = triangle[0]
    # print(dp)
    for layer, nums in enumerate(triangle[1:]):
        # print(layer, nums)

        dp[layer + 1][0] = dp[layer][0] + nums[0]  # first
        for j in range(1, len(nums) - 1):
            dp[layer + 1][j] = max(dp[layer][j], dp[layer][j - 1]) + nums[j]
        dp[layer + 1][-1] = dp[layer][-1] + nums[-1]  # last
        # print(dp)

    return max(dp[-1])

