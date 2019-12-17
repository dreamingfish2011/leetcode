class Solution:
    ##分治法，递归
    def longestCommonPrefixRecursion(self, strs) -> str:
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        if len(strs) == 2:
            i = 0
            while i < len(strs[0]) and i < len(strs[1]) and strs[0][i] == strs[1][i]:
                i += 1
            if i == 0:
                return ""
            else:
                return strs[0][0:i]
        else:
            i = int(len(strs) / 2)
            new_strs = [self.longestCommonPrefixRecursion(strs[0:i]), self.longestCommonPrefixRecursion(strs[i:])]
            return self.longestCommonPrefixRecursion(new_strs)

    ##compare parallel  平行比较
    # 97.34 %  12.9M
    def longestCommonPrefix(self, strs) -> str:
        res_len = 0
        if len(strs) == 0:
            return ""
        while True:
            if len(strs[0]) > res_len:
                pre = strs[0][res_len]
                for i in range(1, len(strs)):
                    if len(strs[i]) <= res_len or pre != strs[i][res_len]:
                        return strs[0][0:res_len]
                res_len += 1
            else:
                return strs[0][0:res_len]
        return strs[0][0:res_len]

    ##use zip  巧用zip
    # Runtime: 32 ms, faster than 99.70% of Python3 online submissions for Longest Common Prefix.
    # Memory Usage: 13.2 MB, less than 5.10% of Python3 online submissions for Longest Common Prefix.
    def longestCommonPrefixUseZip(self, strs) -> str:
        if not strs: return ''
        res_len = 0
        tuples = list(zip(*strs))
        for i in range(len(tuples)):
            if len(set(tuples[i])) == 1:
                res_len += 1
            else:
                break
        return strs[0][0:res_len]

    ##常规方式，两个两个求公共子串
    # 75.28 %   13.2M
    def longestCommonPrefixRegular(self, strs) -> str:
        if not strs: return ''
        if not strs: return ''
        N = len(strs[0])
        if N == 0:
            return ''
        for i in range(N):
            pre = strs[0][i]
            for j in range(1, len(strs)):
                if len(strs[j]) <= i or strs[j][i] != pre:
                    return strs[0][0:i]
        return strs[0]


if __name__ == "__main__":
    test = Solution()
    strs = ["flower", "flow", "flight"]
    print("ouput str=", test.longestCommonPrefix(strs))
    print("ouput str=", test.longestCommonPrefixRecursion(strs))
