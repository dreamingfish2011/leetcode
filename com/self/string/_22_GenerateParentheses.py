class Solution:
    ##递归
    #Runtime: 36 ms, faster than 99.24% of Python3 online submissions for Generate Parentheses.
    #Memory Usage: 13.4 MB, less than 43.24% of Python3 online submissions for Generate Parentheses.
    def generateParenthesis(self, n: int, open=0):
        if n > 0 <= open:
            return ['(' + p for p in self.generateParenthesis(n - 1, open + 1)] + \
                   [')' + p for p in self.generateParenthesis(n, open - 1)]
        return [')' * open] * (not n)

    # 回溯法，从n-1字符串开始切，切后加
    #Runtime: 36 ms, faster than 99.24% of Python3 online submissions for Generate Parentheses.
    #Memory Usage: 13.4 MB, less than 43.24% of Python3 online submissions for Generate Parentheses.
    def generateParenthesisByTrack(self, n: int):
        dp = {1: ['()']}
        if n == 1:
            return dp[1]
        for i in range(2, n + 1):
            result = []
            for cut in range(0, i):
                for pre in dp[i - 1]:
                    if cut == 0:
                        result.append(pre + '()')
                    elif set(pre[-cut:]) == set(')'):
                        currstr = pre[0:-cut] + '(' + ')' * (cut+1)
                        result.append(currstr)
            dp[i] = result
            del dp[i - 1]
        return dp[n]


if __name__ == '__main__':
    t = Solution();
    print(t.generateParenthesisByTrack(50))
