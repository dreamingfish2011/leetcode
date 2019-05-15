class Solution:
    def fib(self, N: int) -> int:
        ge = self.fib_gen(N)
        return ge.__next__

    def fib_gen(self,N):
        a =0
        b =1
        i = 0
        while i < N:
            if i == N-1:
                yield b
            a,b=b,a+b
            i += 1
def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        # print b
        a, b = b, a + b
        n = n + 1

def fabAtN(max):
    n, a, b = 0, 0, 1
    while n < max:
        if n == max-1:
            yield b
            break
        # print b
        a, b = b, a + b
        n = n + 1

if __name__ == "__main__":
    fabs =fab(6)
    for f in fabs:
        print(f)
    generator_fab = fabAtN(7)
    print("yield 类型：",type(generator_fab))
    print(generator_fab.__next__())