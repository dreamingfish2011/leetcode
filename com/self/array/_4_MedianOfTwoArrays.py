import sys


class Solution(object):
    def medianOfTwoArrays(self, nums1, nums2):
        median = 0.0
        an = len(nums1)
        bn = len(nums2)
        i = (int)((an + bn - 1) / 2)
        ai = 0
        bi = 0
        for j in range(i):
            if ai <= an - 1 and (bn == 0 or bi == bn or (bi <= bn - 1 and nums1[ai] <= nums2[bi])):
                ai += 1
            else:
                bi += 1
        if (an + bn) % 2 == 1:
            if ai <= an - 1 and (bn == 0 or bi == bn or (bi <= bn - 1 and nums1[ai] <= nums2[bi])):
                median = nums1[ai]
            else:
                median = nums2[bi]
        else:
            result = nums1[ai:ai + 2] + nums2[bi:bi + 2]
            result = sorted(result)
            median = (result[0] + result[1]) / 2
        return median

    def findMedianSortedArrays(self, nums1, nums2) -> float:
        if len(nums1) == 0:
            return self.findMedianInOneArray(nums2)
        if len(nums2) == 0:
            return self.findMedianInOneArray(nums1)
        n = len(nums1)
        m = len(nums2)
        ##假定nums1是长度小的那个数组
        if n > m:
            return self.findMedianSortedArrays(nums2, nums1)
        L1, R1, L2, R2, c1, c2 = 0, 0, 0, 0, 0, 0
        lo = 0
        hi = 2 * n
        while lo <= hi:
            c1 = int((lo + hi) / 2)
            c2 = m + n - c1
            if c1 == 0:
                L1 = -1 * sys.maxsize - 1
            else:
                L1 = nums1[int((c1 - 1) / 2)]
            if c1 == 2 * n:
                R1 = sys.maxsize
            else:
                R1 = nums1[int(c1 / 2)]
            if c2 == 0:
                L2 = -1 * sys.maxsize - 1
            else:
                L2 = nums2[int((c2 - 1) / 2)]
            if c2 == 2 * m:
                R2 = sys.maxsize
            else:
                R2 = nums2[int(c2 / 2)]
            if L1 > R2:
                hi = c1 - 1
            if L2 > R1:
                lo = c1 + 1
            ##找到中位数
            if L1 <= R2 and L2 <= R1:
                break
        ##最后返回时候，如果是奇数，相当于返回中位数两次，即L1==R1或者L2==R2
        return (max(L1, L2) + min(R1, R2)) / 2.0

    def findMedianInOneArray(self, nums):
        if len(nums) == 0:
            return -1
        return (nums[int(len(nums) / 2)] + nums[int((len(nums) - 1) / 2)]) / 2


if __name__ == "__main__":
    test = Solution()
    a1 = [1, 2]
    a2 = [3, 4, 5]
    print(test.findMedianSortedArrays(a1, a2))
