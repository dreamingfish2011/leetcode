import collections


class Solution:
    def fourSumCount(self, A, B, C, D) -> int:
        AB = collections.Counter(a + b for a in A for b in B)
        return sum(AB[-c - d] for c in C for d in D)


if __name__ == "__main__":
    test = Solution()
    A = [1, 2]
    B = [-2, -1]
    C = [-1, 2]
    D = [0, 2]
    print(test.fourSumCount(A, B, C, D))
