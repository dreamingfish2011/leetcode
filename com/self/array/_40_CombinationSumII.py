class Solution:
    def combinationSum2(self, candidates, target: int):
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
            # self.dfs(candidates, target - candidates[index], i + 1, path + [candidates[index]], result)
            if i > index and candidates[i - 1] == candidates[i]:
                continue
            else:
                path = path + [candidates[i]]
                self.dfs(candidates, target - candidates[i], i + 1, path, result)
                path = path[:-1]


if __name__ == '__main__':
    t = Solution()
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    print(t.combinationSum2(candidates, target))
