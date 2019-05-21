import time
class Solution:
    #easy
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        if m == 0:
            return 0
        i=0
        j=0
        while i <n and j <m:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                i = i-j+1
                j =0
        if j == m :
            return i-j
        else :
            return -1
    #kmp
    def strStrByKMP(self, haystack: str, needle: str) -> int:
        if haystack == None or needle == None:
            return -1
        #generate next array, need O(n) time
        i, j, m, n = -1, 0, len(haystack), len(needle)
        next = [-1] * n
        while j < n - 1:
            #needle[k] stands for prefix, neelde[j] stands for postfix
            if i == -1 or needle[i] == needle[j]:
                i, j = i + 1, j + 1
                next[j] = i
            else:
                i = next[i]
            # print(i,j,next[i],next[j])
        #check through the haystack using next, need O(m) time
        i = j = 0
        while i < m and j < n:
            if j == -1 or haystack[i] == needle[j]:
                i, j = i + 1, j + 1
            else:
                j = next[j]
        if j == n:
            return i - j
        return -1
    ###another
    def strStrAnotherKMP(self, haystack: str, needle: str) -> int:
        if not needle: return 0
        if not haystack: return -1

        next_arr = self.create_next(needle)
        i = j = 0

        while i < len(haystack) and j < len(needle):
            if haystack[i] == needle[j]:
                # Matched, so return the haystack's match start index.
                if j == len(needle) - 1:
                    return i - len(needle) + 1
                i, j = i + 1, j + 1
            else:
                # Slide pattern over.
                if j: j = next_arr[j-1]
                else: i += 1

        return -1

    # Build next jump table.
    def create_next(self, pattern):
        next_arr = [0] * len(pattern)
        pre_i, suf_i = 0, 1

        while suf_i < len(pattern):
            # Found prefix-suffix match.
            if pattern[pre_i] == pattern[suf_i]:
                next_arr[suf_i] = pre_i + 1
                pre_i, suf_i = pre_i + 1, suf_i + 1
            else:
                if pre_i:
                    pre_i = next_arr[pre_i-1]
                else:
                    next_arr[suf_i] = 0
                    suf_i += 1

        return next_arr
if __name__ == '__main__':
    t = Solution();
    haystack= "abcdabdabcdabdabcdabdabcdabdabcdababcdabdabcdabdabcdabdabcdabdabcdababcdabdabcdabdabcdabdabcdabdabcdababcdabdabcdabdabcdabdabcdabdabcdababcdabdabcdabdabcdabdabcdabdabcdababcdabdabcdabdabcdabdabcdabdabcdababcdabdabcdabdabcdabdabcdabdabcdababcdabdabcdabdabcdabdabcdabdabcdababcdabdabcdabdabcdabdabcdabdabcdababcdabdabcdabdabcdabdabcdabdabcdababcdabdabcdabdabcdabdabcdabdabcdababcdabdabcdabdabcdabdabcdabdabcdababcdabdabcdabdabcdabdabcdabdabcdababcdabdabcdabdabcdabdabcdabdabcdababcdabdabcdabdabcdabdabcdabdabcdababcdabdabcdabdabcdabdabcdabdabcdababcdabdabcdabdabcdabdabcdabdabcdabdabcdabdabcdabdabcdabdabcdabc"
    needle ="abcdabc"
    print(time.time())
    print(t.strStrByKMP(haystack,needle))
    print(time.time())
    print(t.strStr(haystack,needle))
    print(time.time())


