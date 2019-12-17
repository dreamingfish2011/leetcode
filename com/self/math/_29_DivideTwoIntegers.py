class Solution:
    #minus实现
    #左移实现循环减，1,2,4,8,16...倍的divisor。每次减几倍res就加几
    def divide(self, dividend: int, divisor: int) -> int:
        positive = (dividend < 0) is (divisor < 0)
        ##超出时候-2147483648，这里有问题
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)


if __name__ == '__main__':
    t = Solution();
    print(t.divide(10, 3))
