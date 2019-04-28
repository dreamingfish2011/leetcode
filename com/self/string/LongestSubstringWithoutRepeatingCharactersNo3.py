class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict_ss ={}
        maxLen = 0
        i =0
        j=0
        #区间  i  --  j
        while i <len(s) and j<len(s):
            if s[j] not in dict_ss:
                dict_ss[s[j]] = j
                j +=1
                maxLen = max(maxLen,j-i)
            else :
                del dict_ss[s[i]]
                i +=1
        return maxLen

if __name__ == "__main__":
    test = Solution()
    s = "abcabcadfgfd"
    print(test.lengthOfLongestSubstring(s))