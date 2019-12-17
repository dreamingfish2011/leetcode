class Solution:
    def nextPermutation(self, nums) -> None:
        i = len(nums) - 2
        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            self.swap(nums, i, j)
        nums[i+1:] = nums[i+1:][::-1]
        # self.reverse(nums, i + 1)

    def swap(self, nums, i, j):
        temp_i = nums[i]
        temp_j = nums[j]
        nums[i] = temp_j
        nums[j] = temp_i


if __name__ == '__main__':
    t = Solution();
    nums = [1, 3, 2]
    t.nextPermutation(nums)
    # nums = nums[::-1]
    print(nums)
