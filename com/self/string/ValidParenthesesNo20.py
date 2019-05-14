class Solution:
    def isValid(self, s: str) -> bool:
        stacks = []
        dic_valid = {'}': '{', ']': '[', ')': '('}
        for item in s:
            if item in ['(', '{', '[']:
                stacks.append(item)
            else:
                if len(stacks) == 0:
                    return False
                elif stacks.pop() != dic_valid[item]:
                    return False
        if len(stacks) ==0:
            return True
        else:
            return False


if __name__ == '__main__':
    t = Solution();
    print(t.isValid("())({}{}}{"))
