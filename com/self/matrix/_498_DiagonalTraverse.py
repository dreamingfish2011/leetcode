class Solution:
    def findDiagonalOrder(self, matrix )  :
        rel = []
        M = len(matrix)
        if M ==0:
            return rel
        N = len(matrix[0])
        if M ==0:
            return rel
        i = 0
        j = 0
        for X in range(0,M*N) :
            rel.append(matrix[j][i])
            if (i + j) % 2 == 0: #moving up
                if  i == N - 1:
                    j +=1
                elif j == 0:
                    i +=1
                else:
                    j -=1
                    i +=1
            else: #moving down
                if j == M - 1:
                    i +=1
                elif i == 0:
                    j +=1
                else:
                    j +=1
                    i -=1
        return rel
if __name__ == "__main__":
    test = Solution()
    a = [
        [ 1, 2, 3 ],
        [ 4, 5, 6 ],
        [ 7, 8, 9 ]
    ]
    print(test.findDiagonalOrder(a))