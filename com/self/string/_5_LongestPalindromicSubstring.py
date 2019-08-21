class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # -------------------------------
        # \         \             \
        # 预处理 Manacher算法
        s = '#' + '#'.join(s) + '#'

        RL = [0] * len(s)
        MaxRight = 0
        pos = 0
        MaxLen = 0
        final_pos = 0
        for i in range(len(s)):
            if i < MaxRight:
                RL[i] = min(RL[2 * pos - i], MaxRight - i)
            else:
                RL[i] = 1
            # 尝试扩展，注意处理边界
            while i - RL[i] >= 0 and i + RL[i] < len(s) and s[i - RL[i]] == s[i + RL[i]]:
                RL[i] += 1
            # 更新MaxRight,pos
            if RL[i] + i - 1 > MaxRight:
                MaxRight = RL[i] + i - 1
                pos = i
            # 更新最长回文串的长度
            MaxLen = max(MaxLen, RL[i])
        subs = s[pos - MaxLen + 1:pos + MaxLen - 1]
        return subs.replace('#', '')
        # return MaxLen-1
    ##动态规划
    def longestPalindromeByDP(self, s):
        K = len(s)
        last_dp = [0] * K
        curr_dp = [0] * K
        maxLength, max_i = 0, 0
        for j in range(0, K):
            for i in range(0, j + 1):
                if j - i <= 1:
                    if s[i] == s[j]:
                        curr_dp[i] = 1
                        if j - i + 1 > maxLength:
                            maxLength = j - i + 1
                            max_i = i
                else:
                    if s[i] == s[j] and last_dp[i + 1] == 1:
                        curr_dp[i] = 1
                        if j - i + 1 > maxLength:
                            maxLength = j - i + 1
                            max_i = i
            last_dp = curr_dp
            curr_dp = [0] * K
        return s[max_i:max_i + maxLength]


if __name__ == "__main__":
    test = Solution()

    print(test.longestPalindrome('abba'))
    print(test.longestPalindromeByDP('babad'))
