class Solution:
    ##递归recursion method  DFS
    #Runtime: 36 ms, faster than 85.77 %  of Python3 online submissions for Letter Combinations of a Phone Number.
    #Memory Usage: 13.3 MB, less than 5.86% of Python3 online submissions for Letter Combinations of a Phone Number.
    def letterCombinations(self, digits: str) :
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        result = []

        def helpCombine(current, leftoverDigits):
            if not leftoverDigits:
                result.append(current)
                return
            else:
                for char in phone[leftoverDigits[0]]:
                    helpCombine(current + char, leftoverDigits[1:])

        if not digits:
            return []
        else:
            helpCombine("", digits)
            return result
    #DFS
    #Runtime: 32 ms, faster than 98.79% of Python3 online submissions for Letter Combinations of a Phone Number.
    #Memory Usage: 13.2 MB, less than 5.86% of Python3 online submissions for Letter Combinations of a Phone Number.
    def letterCombinationsByDFS(self, digits: str) :
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        result = ['']
        if not digits:
            return []
        else:
            for digit in digits:
                res =[]
                for s in result:
                    for letter in phone[digit]:
                        res.append(s+letter)
                result = res
            return result
if __name__ == '__main__':
    t =Solution();
    print(t.letterCombinationsByDFS("234"))