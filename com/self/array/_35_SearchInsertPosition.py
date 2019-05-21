class Solution:
    # Runtime: 28 ms, faster than 99.70% of Python3 online submissions for Search Insert Position.
    # Memory Usage: 13.7 MB, less than 33.67% of Python3 online submissions for Search Insert Position.
    def searchInsert(self, nums, target: int) -> int:
        lo = 0
        hi = len(nums) - 1
        flag = 0
        while lo <= hi:
            mid = int((lo + hi) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                if mid + 1 <= hi and nums[mid + 1] > target:
                    return mid + 1
                else:
                    lo = mid + 1
            else:
                if mid - 1 >= 0 and nums[mid - 1] < target:
                    return mid
                else:
                    hi = mid - 1
        return lo


if __name__ == '__main__':
    t = Solution();
    nums = [1, 3, 5, 6]
    target = 8
    print(t.searchInsert(nums, target))
