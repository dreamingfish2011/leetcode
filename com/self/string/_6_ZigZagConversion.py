#蜿蜒字符串
#思路很简单，目标是几行就申请几个字符串变量。
#从头到尾访问字符串，step记录方向，+1表示从前往后加入L，-1表示从后往前加入L
#时间复杂度 O(n)   空间复杂度  O(n)
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        L = [''] * numRows
        index, step = 0, 1

        for x in s:
            L[index] += x
            if index == 0:
                step = 1
            elif index == numRows -1:
                step = -1
            index += step

        return ''.join(L)
if __name__ == "__main__":
    test = Solution()
    print(test.convert("DLGFKDSFHJKAFUREINGDJFGJDKKL",5))