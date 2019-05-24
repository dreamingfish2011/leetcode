class Solution:
    # brief code
    # Runtime: 164 ms, faster than 37.73% of Python3 online submissions for Multiply Strings.
    # Memory Usage: 13.1 MB, less than 73.83% of Python3 online submissions for Multiply Strings.
    def multiply1(self, num1, num2):
        res = [0] * (len(num1) + len(num2))
        for i in range(len(num1) - 1, -1, -1):
            carry = 0
            for j in range(len(num2) - 1, -1, -1):
                tmp = int(num1[i]) * int(num2[j]) + carry
                carry = (res[i + j + 1] + tmp) // 10
                res[i + j + 1] = (res[i + j + 1] + tmp) % 10
            res[i] += carry
        res = "".join(map(str, res))
        return '0' if not res.lstrip("0") else res.lstrip("0")

    # time over limit
    def multiply(self, num1: str, num2: str) -> str:
        if len(num1) == 0 or len(num2) == 0:
            return ""
        if num1[0] == "0" or num2[0] == "0":
            return "0"
        result = ""
        j = 0
        for a in range(len(num2) - 1, -1, -1):
            i = 0
            iner_rel = "0"
            for b in range(len(num1) - 1, -1, -1):
                be_added = str(int(num1[b]) * int(num2[a])) + "0" * i
                iner_rel = self.addString(iner_rel, be_added)
                i += 1
            iner_rel = iner_rel + "0" * j
            result = self.addString(result, iner_rel)
            j += 1
        return result

    def addString(self, curr_str, be_added):
        curr_len = len(be_added)
        last_len = len(curr_str)
        carry = 0
        i = 0
        for s in range(curr_len - 1, -1, -1):
            last = int(curr_str[last_len - 1 - i]) if i < last_len else 0
            add = int(be_added[s])
            be_added = be_added[0:s] + str((carry + last + add) % 10) + be_added[s + 1:]
            if carry + last + add >= 10:
                carry = 1
            else:
                carry = 0
            i += 1
        if carry == 1:
            be_added = "1" + be_added
        return be_added


if __name__ == '__main__':
    t = Solution()
    num1 = "17713693108358378680072681827220994275895642679450569947042064076615194860248215"
    num2 = "6157728148710697840711533037191926601417410571458451704108837221091155108177315170452863668581"
    print(t.multiply1(num1, num2))
    print(t.multiply(num1, num2))
