class Solution:
    #Runtime: 40 ms, faster than 87.40% of Python3 online submissions for Count and Say.
    #Memory Usage: 13.2 MB, less than 46.29% of Python3 online submissions for Count and Say.
    def countAndSay(self, n: int) -> str:
        gen = self.generateCountAndSay(n)
        rel =""
        for item in gen:
            rel =item
        # print(next(gen))
        return rel

    def generateCountAndSay(self, n):
        cas = "1"
        i = 0
        while i < n:
            yield cas
            count = 0
            rel = ""
            pre = cas[0]
            for c in cas:
                if pre == c:
                    count += 1
                else:
                    rel += str(count) + pre
                    count = 1
                    pre = c
            if count > 0:
                rel += str(count) + pre
            cas = rel
            i = i + 1


if __name__ == '__main__':
    t = Solution()
    print(t.countAndSay(6))
