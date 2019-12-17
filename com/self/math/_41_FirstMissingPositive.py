class Solution:
    def firstMissingPositive(self, nums):
        if len(nums) == 0:
            return 1
        for i in range(0, len(nums)):
            if nums[i] == i + 1 or nums[i] <= 0 or nums[i] > len(nums):
                continue
            while (nums[i] > 0 and nums[i] < i + 1 and nums[i] != nums[nums[i] - 1]):
                temp = nums[nums[i] - 1]
                nums[nums[i] - 1] = nums[i]
                nums[i] = temp
        for i in range(0, len(nums)):
            if (nums[i] != i + 1):
                return i + 1
        return len(nums) + 1
if __name__ == '__main__':
    t = Solution()
    nums = [4,3,2,1]
    print(t.firstMissingPositive(nums))
