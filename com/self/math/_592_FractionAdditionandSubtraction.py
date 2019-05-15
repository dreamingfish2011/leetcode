import re
import math
class Solution:
    def fractionAddition(self, expression: str) -> str:
        ints = map(int, re.findall('[+-]?\d+', expression))
        A, B = 0, 1
        for a in ints:
            b = next(ints)
            A = A * b + a * B
            B *= b
            g = math.gcd(A, B)
            A //= g
            B //= g
        return '%d/%d' % (A, B)
if __name__ == "__main__":
    test = Solution()
    print(test.fractionAddition("-1/2+1/2+1/3"))