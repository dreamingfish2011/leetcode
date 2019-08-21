import sys
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        reverse = 0
        y = x
        while x != 0 :
            tail = x%10
            if reverse > sys.maxsize/10 or (reverse == sys.maxsize/10 and tail > 7):
                return False
            reverse = 10*reverse + tail
            x = int(x/10)
        return y == reverse

    def isPalindromeUseStr(self, x: int) -> bool:
        s= str(x)
        i ,j= 0,len(s)-1
        while i <= j:
            if s[i] == s[j]:
                i +=1
                j-=1
            else:
                return False
        return True


if __name__ == "__main__":
    test = Solution()
    print(test.isPalindrome(15551))
    print(test.isPalindromeUseStr(15551))