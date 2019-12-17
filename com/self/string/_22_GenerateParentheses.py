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
            for pre in dp[i - 1]:
                for cut in range(0, i):
                    if cut == 0:
                        result.append(pre + '()')
                    elif set(pre[-cut:]) == set(')'):
                        currstr = pre[0:-cut] + '(' + ')' * (cut+1)
                        result.append(currstr)
                    else:
                        break
            dp[i] = result
            del dp[i - 1]
        return dp[n]

    def generateParenthesisByBacktrack(self, n: int) :
        ans = []
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * n:
                ans.append(S)
                return
            if left < n:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)

        backtrack()
        return ans


if __name__ == '__main__':
    t = Solution();
    print(len(t.generateParenthesisByTrack(7)))
    print(t.generateParenthesisByBacktrack(7))
