#首先，我们考虑如何确定第一个数left，这肯定是我们第一层循环。
# 第一个数可不能无限制的随便选，因为我们要保证上面的几个条件都满足，
# 我们要保证它时刻是最小的数，那么我们可以考虑left取到全部非正数就行了。（如果要和为0，至少要有1个非正数）
# 然后就是mid和right的确定了，我们采用思路2的方案，mid和right分别从两端往中央扫描，
# 如果mid+right还比较小，那就需要mid右移，反之right左移

class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()
        for left in range(len(nums)-2):
            if nums[left] > 0 :
                break
            if left > 0 and nums[left] == nums[left-1]:
                continue
            mid = left +1
            right = len(nums) -1
            while mid < right :
                target = nums[left] + nums[mid] +nums[right]
                if target == 0 :
                    res.append([nums[left] , nums[mid] ,nums[right]])
                    tmp_mid = nums[mid]
                    tmp_right = nums[right]
                    mid +=1
                    right -=1
                    while mid < right and nums[mid] == tmp_mid : mid +=1
                    while mid < right and nums[right] == tmp_right : right -=1
                elif target <0 :
                    mid += 1
                else :
                    right -=1
        return res
if __name__ == "__main__":
    test = Solution()
    nums =[-1, 0, 1, 2, -1, -4]
    print(test.threeSum(nums))
