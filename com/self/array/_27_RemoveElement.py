class Solution:
    def removeElement(self, nums , val: int) -> int:
        pos = 0
        for i in range(0,len(nums)):
            if nums[i] != val :
                nums[pos] = nums[i]
                pos +=1
        return pos
if __name__ == '__main__':
    test = Solution()
    nums = [-1, 2, 1, -4]
    val = -1
    print(test.removeElement(nums, val))
    print(nums)
