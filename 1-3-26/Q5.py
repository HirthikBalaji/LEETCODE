def minTime(skill, mana):
    n = len(skill)
    m = len(mana)

    # dp[i] = finish time of wizard i for the current potion
    dp = [0] * n

    for j in range(m):
        # wizard 0 must wait for previous potion AND process current one
        dp[0] = dp[0] + skill[0] * mana[j]

        for i in range(1, n):
            # must wait for:
            # 1) wizard i finishing previous potion (dp[i])
            # 2) wizard i-1 finishing current potion (dp[i-1])
            dp[i] = max(dp[i], dp[i - 1]) + skill[i] * mana[j]

    return dp[-1]