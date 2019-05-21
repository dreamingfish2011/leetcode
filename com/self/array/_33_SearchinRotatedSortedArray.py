import sys


class Solution:
    # Runtime: 32 ms, faster than 99.11% of Python3 online submissions for Search in Rotated Sorted Array.
    # Memory Usage: 13.1 MB, less than 80.15% of Python3 online submissions for Search in Rotated Sorted Array.
    def search(self, nums, target: int) -> int:
        n = len(nums)
        left = 0
        right = n

        while left < right:
            mid = int((left + right) / 2)
            num = 0
            ##mid值和target值在同一side
            if (nums[mid] < nums[0]) == (target < nums[0]):
                num = nums[mid]
            # target =3   [4,5,6,7,0,1,2] -->[-inf,-inf,-inf,-inf,0,1,2]
            elif target < nums[0]:
                num = -sys.maxsize - 1
            else:
                num = sys.maxsize
            if num < target:
                left = mid + 1
            elif num > target:
                right = mid
            else:
                return mid
        return -1


if __name__ == '__main__':
    t = Solution();
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    print(t.search(nums, target))
