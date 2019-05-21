class Solution:
    # Runtime: 116 ms, faster than 82.68% of Python3 online submissions for Group Anagrams.
    # Memory Usage: 16 MB, less than 62.26% of Python3 online submissions for Group Anagrams.
    def groupAnagramsByHash(self, strs):
        res = {}
        prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103]
        for item in strs:
            dict_key = 1
            for c in item:
                dict_key *= prime[ord(c) - ord('a')]
            if dict_key in res:
                res[dict_key] = res.get(dict_key) + [item]
            else:
                res[dict_key] = [item]
        return list(res.values())

    # Runtime: 108 ms, faster than 97.75% of Python3 online submissions for Group Anagrams.
    # Memory Usage: 15.7 MB, less than 83.25% of Python3 online submissions for Group Anagrams.
    def groupAnagramsBySort(self, strs):
        res = {}
        for item in strs:
            dict_key = "".join(sorted(item))
            if dict_key in res:
                res[dict_key] = res.get(dict_key) + [item]
            else:
                res[dict_key] = [item]
        return list(res.values())


if __name__ == '__main__':
    t = Solution();
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(t.groupAnagramsByHash(strs))
