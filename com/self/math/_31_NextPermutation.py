class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = -1
        l = 0
        for k in range(n - 2, -1, -1):
            if nums[k] < nums[k + 1]:
                break
        if k <= 0:
            nums = nums[::-1]
            # nums.sort()
        else:
            for l in range(n - 1, k, -1):
                if nums[l] > nums[k]:
                    break
            nums[k], nums[l] = nums[l], nums[k]
            nums[k + 1:n] = nums[k + 1:n][::-1]
        print(nums)


if __name__ == '__main__':
    t = Solution();
    nums = [1, 2]
    t.nextPermutation(nums)
    # nums = nums[::-1]
    # print(nums)
