#先排序
#确定一个数，然后文件顺利变成3SUM问题，然后就是完完全全3SUM的解决思路了。
class Solution(object):
    def fourSum(self, nums, target):
        res = []
        nums.sort()
        for i in range(0, len(nums) - 3):
            target_i = target - nums[i]
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for left in range(i + 1, len(nums) - 2):
                if left > i +1 and nums[left] == nums[left - 1]:
                    continue
                mid = left + 1
                right = len(nums) - 1
                while mid < right:
                    curr_sum = nums[left] + nums[mid] + nums[right]
                    if target_i == curr_sum:
                        res.append([nums[i], nums[left], nums[mid], nums[right]])
                        tmp_mid = nums[mid]
                        tmp_right = nums[right]
                        mid += 1
                        right -= 1
                        while mid < right and nums[mid] == tmp_mid: mid += 1
                        while mid < right and nums[right] == tmp_right: right -= 1
                    elif target_i > curr_sum:
                        mid += 1
                    else:
                        right -= 1
        return res


if __name__ == "__main__":
    test = Solution()
    nums = [1, 0, -1, 0, -2, 2]
    print(test.fourSum(nums, 0))
