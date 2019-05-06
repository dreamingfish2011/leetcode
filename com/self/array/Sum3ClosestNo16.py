#然后还是mid和right分别从两端往中央扫描，如果mid+right还比较小，
# 那就需要mid右移，反之right左移（每次如果有最小的就存下来）
class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        if len(nums) < 3:
            return 0
        min_return = nums[0] + nums[1] + nums[2]
        if target - min_return <= 0:
            return nums[0] + nums[1] + nums[2]

        for left in range(len(nums) - 2):
            mid = left + 1
            right = len(nums) - 1
            while mid < right:
                tmp = target - nums[left]
                if abs(tmp- nums[mid] - nums[right]) < abs(target - min_return):
                    min_return = nums[left] + nums[mid] + nums[right]
                if tmp == nums[mid] + nums[right]:
                    return target
                elif tmp > nums[mid] + nums[right]:
                    mid += 1
                else:
                    right -= 1

        return min_return

if __name__ == "__main__":
    test = Solution()
    nums = [-1, 2, 1, -4]
    print(test.threeSumClosest(nums, 1))
