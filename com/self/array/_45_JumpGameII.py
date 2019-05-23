class Solution:
    def jump1(self, nums):
        n, cur_max, next_max, steps = len(nums), 0, 0, 0
        for i in range(n):
            if i > cur_max:
                steps += 1
                cur_max = next_max
                if cur_max >= n: break
            next_max = max(next_max, nums[i] + i)
        return steps

    def jump(self, nums) -> int:
        target = [num + i for i, num in enumerate(nums)]
        count = 0
        pos = 0
        n = len(nums)
        while pos < n - 1:
            pos = self.getNextPos(nums, target, pos)
            if pos == -1:
                return 0
            count += 1
        return count

    def getNextPos(self, nums, target, pos):
        tail = min(len(nums) - 1, pos + nums[pos])
        rel = -1
        max_target = 0
        for i in range(tail, pos, -1):
            if target[i] >= len(nums) - 1:
                return i
            if target[i] >= max_target:
                max_target = target[i]
                rel = i
        return rel


if __name__ == '__main__':
    t = Solution()
    nums = [2, 3, 1, 1, 4]
    print(t.jump(nums))
