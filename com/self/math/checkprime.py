from math import sqrt


class Solution:
    def is_prime(self, n):
        if n <= 3:
            return True
        # 因为6的倍数+2可以被2整除，6的倍数+3可以被3整除，6的倍数+4可以被2整除，6的倍数可以被6整除
        # 所以只有n = 6的倍数+1或者+5才有可能是素数
        if n % 6 != 1 and n % 6 != 5:
            return False
        # 除此之外，还要判断该数可否被6的倍数+1或者+5整除
        # 比如25虽然在24（4*6）的右边，但它可以被5（0+5）整除
        # 比如49虽然在48（8*6）的右边，但它可以被7（6+1）整除
        for i in range(5, int(sqrt(n) + 1), 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False
        return True


if __name__ == '__main__':
    t =Solution();
    print(t.is_prime(15))
