class Solution:
    def combinationSum(self, candidates, target: int):
        result = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], result)
        return result

    def dfs(self, candidates, target, index, path, result):
        if target < 0:
            return
        if target == 0:
            result.append(path)
            return
        for i in range(index, len(candidates)):
            num = candidates[i]
            self.dfs(candidates, target - num, i, path + [num], result)


if __name__ == '__main__':
    t = Solution()
    candidates = [2, 3, 5]
    target = 7
    print(t.combinationSum(candidates, target))
