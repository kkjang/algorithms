#recursive, no memoization
def longest_common_subsequence(str1, str2, i=None, j=None):
    if i is None:
        i = len(str1)-1
    if j is None:
        j = len(str2)-1
    if i < 0 or j < 0:
        return 0
    if str1[i] == str2[j]:
        return 1 + longest_common_subsequence(str1, str2, i-1, j-1)
    else:
        return max(longest_common_subsequence(str1, str2, i-1, j), longest_common_subsequence(str1, str2, i, j-1))

def longest_common_subsequence_dp(str1, str2):
    dp = [[False]*len(str2) for _ in range(len(str1))]
    for i in range(len(str2)):
        dp[0][i] = str1[0] == str2[i]
    for i in range(len(str1)):
        dp[i][0] = str1[i] == str2[0]

    for row in range(1, len(str1)):
        for col in range(1, len(str2)):
            if str1[row] == str2[col]:
                dp[row][col] = dp[row-1][col-1] + 1
            else:
                dp[row][col] = max(dp[row-1][col], dp[row][col-1])
    return dp[len(str1)-1][len(str2)-1]


print(longest_common_subsequence_dp("aggtab", "gxtxayab"))
