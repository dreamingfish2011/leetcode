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


if __name__ == "__main__":
    test = Solution()
    print(test.isPalindrome(15551))