class Solution:
    #Runtime: 36 ms, faster than 97.25% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
    #Memory Usage: 13.9 MB, less than 43.91% of Python3 online submissions for Find First and Last Position of
    # Element in Sorted Array.
    def searchRange(self, nums, target: int):
        lo = 0
        hi = len(nums) - 1
        left = -1
        right = -1
        while lo <= hi:
            mid = int((lo + hi) / 2)
            if nums[mid] == target:
                left = mid
                hi = mid - 1
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        if left > -1:
            lo = 0
            hi = len(nums) - 1
            while lo <= hi:
                mid = int((lo + hi) / 2)
                if nums[mid] == target:
                    right = mid
                    lo = mid + 1
                elif nums[mid] > target:
                    hi = mid - 1
                else:
                    lo = mid + 1
        return [left, right]


if __name__ == '__main__':
    t = Solution();
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    print(t.searchRange(nums, target))
