class Solution:
    # Runtime: 56 ms, faster than 99.12% of Python3 online submissions for Substring with Concatenation of All Words.
    # Memory Usage: 13 MB, less than 85.46% of Python3 online submissions for Substring with Concatenation of All Words.
    def findSubstring(self, s: str, words):
        if len(words) == 0:
            return []
        # initialize d, l, ans
        step = len(words[0])
        d = {}
        res = []
        for w in words:
            d[w] = d.get(w, 0) + 1
        for i in range(step):
            left = i
            iner_d = {}
            count = 0
            for j in range(i, len(s) + 1 - step, step):
                curr_word = s[j:j + step]
                if curr_word in d:
                    iner_d[curr_word] = iner_d.get(curr_word, 0) + 1
                    count += 1
                    while iner_d[curr_word] > d[curr_word]:
                        iner_d[s[left:left + step]] -= 1
                        left += step
                        count -= 1
                    if count == len(words):
                        res.append(left)
                else:
                    left = j + step
                    iner_d = {}
                    count = 0
        return res


if __name__ == '__main__':
    t = Solution();
    s = "barfoothefoobarman"
    words = ["foo", "bar"]
    print(t.findSubstring(s, words))
