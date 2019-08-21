class Solution:
    def reverse(self, x: int) -> int:
        MaxSize = 2 ** 31
        MinSize = -2 ** 31
        rev = 0
        while x:
            pop = x % 10
            if x < 0 and pop:
                pop -= 10
            x = int(x / 10)
            # -2147483648
            if rev > int(MaxSize / 10) or (rev == int(MaxSize / 10) and pop > 7):
                return 0
            if rev < int(MinSize / 10) or (rev == int(MinSize / 10) and pop < -8):
                return 0
            rev = rev * 10 + pop
        return rev


if __name__ == '__main__':
    t = Solution()
    ratings = -10
    result = t.reverse(ratings)
    print(result)
