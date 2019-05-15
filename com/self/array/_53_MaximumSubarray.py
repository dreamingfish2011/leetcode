class Solution:
    def maxSubArray(self, nums ) -> int:
        keepMax = nums[0]
        maxSum =nums[0]
        for i in range(1,len(nums)):
            if keepMax < 0 :
                keepMax = 0
            keepMax += nums[i]
            maxSum = max(maxSum,keepMax)
        return maxSum

if __name__ == '__main__':
    t = Solution()
    a = [-1, 3, -8, 7, 50, -1, -1]
    print(t.maxSubArray(a))
