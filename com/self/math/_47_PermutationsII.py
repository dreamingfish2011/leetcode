class Solution:
    def permuteUnique(self, nums):
        nums.sort()
        return self.permute(nums)

    def permute(self, nums):
        return [[n] + p
                for i, n in enumerate(nums) if i == 0 or nums[i] != nums[i - 1]
                for p in self.permute(nums[:i] + nums[i + 1:])] or [[]]


if __name__ == '__main__':
    t = Solution();
    nums = [1, 2, 1, 2]
    print(t.permuteUnique(nums))
