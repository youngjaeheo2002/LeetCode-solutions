#https://leetcode.com/problems/spiral-matrix/submissions/1171858604/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        print(matrix)
        if not matrix:
            return []

        if not matrix[0]:
            return []

        if len(matrix) == 1:
            return matrix[0]

        if len(matrix[0]) == 1:
            flattened_matrix = [element for row in matrix for element in row]
            return flattened_matrix
        output = []

        for i in range(len(matrix[0])):
            output.append(matrix[0][i])

        for j in range(1,len(matrix)):
            print(j)
            output.append(matrix[j][-1])


        for i in range(len(matrix[0])-2,-1,-1):
            output.append(matrix[-1][i])

        for i in range(len(matrix)-2,0,-1):
            output.append(matrix[i][0])

        trimmed_matrix = [row[1:-1] for row in matrix[1:-1]]
        return output + self.spiralOrder(trimmed_matrix)

