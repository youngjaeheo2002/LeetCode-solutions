class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        import numpy as np
        matrix = np.zeros((m,n))


        for i in range(n):
            matrix[0][i] = 1

        for i in range(m):
            matrix[i][0] = 1

        for i in range(1,n):
            for j in range(1,m):
                matrix[j][i] = matrix[j-1][i] + matrix[j][i-1]

        return int(matrix[m-1][n-1])
