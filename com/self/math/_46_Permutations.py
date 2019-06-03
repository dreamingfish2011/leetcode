import copy


class Solution:
    # https://leetcode.com/problems/permutations/discuss/18241/One-Liners-in-Python
    # Solution 2: Recursive, insert first number anywhere
    # Insert the first number anywhere in any permutation of the remaining numbers.
    # Runtime: 36 ms, faster than 99.99% of Python3 online submissions for Permutations.
    # Memory Usage: 13.2 MB, less than 52.72% of Python3 online submissions for Permutations.
    def permute(self, nums):
        return nums and [p[:i] + [nums[0]] + p[i:]
                         for p in self.permute(nums[1:])
                         for i in range(len(nums))] or [[]]

    # Solution 1: Recursive, take any number as first
    # Runtime: 52 ms, faster than 80.45% of Python3 online submissions for Permutations.
    # Memory Usage: 13.2 MB, less than 56.00% of Python3 online submissions for Permutations.
    def permute1(self, nums):
        return [[n] + p
                for i, n in enumerate(nums)
                for p in self.permute1(nums[:i] + nums[i + 1:])] or [[]]

    # Runtime: 60 ms, faster than 23.24% of Python3 online submissions for Permutations.
    # Memory Usage: 12.8 MB, less than 88.04% of Python3 online submissions for Permutations.
    def permute(self, nums):
        result = []
        nums.sort()
        result.append(copy.deepcopy(nums))
        n = len(nums)
        while True:
            l = 0
            k = -1
            for k in range(n - 2, -2, -1):
                if k == -1: break
                if nums[k] < nums[k + 1]:
                    break
            if k == -1:
                break
            else:
                for l in range(n - 1, k, -1):
                    if nums[l] > nums[k]:
                        break
                nums[l], nums[k] = nums[k], nums[l]
                nums[k + 1:n] = nums[k + 1:n][::-1]
                result.append(copy.deepcopy(nums))
        return result


if __name__ == '__main__':
    t = Solution();
    nums = [1, 2, 3]
    print(t.permute(nums))
