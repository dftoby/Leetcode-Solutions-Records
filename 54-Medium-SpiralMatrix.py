class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        # --- My Solution ---
        m = [i for i in range(len(matrix))]
        n = [i for i in range(len(matrix[0]))]

        visit_m = 0
        visit_n = 0

        result = []

        while True:

            # Visit right
            for visit_n in n:
                result.append(matrix[visit_m][visit_n])
            if len(result) >= len(matrix)*len(matrix[0]):
                break
            else:
                del m[0]
            print(result,m,n)
            
            # Visit down
            for visit_m in m:
                result.append(matrix[visit_m][visit_n])
            if len(result) >= len(matrix)*len(matrix[0]):
                break
            else:
                del n[-1]
            print(result,m,n)
            
            # Visit left
            for visit_n in n[::-1]:
                result.append(matrix[visit_m][visit_n])
            if len(result) >= len(matrix)*len(matrix[0]):
                break
            else:
                del m[-1]
            print(result,m,n)

            # Visit up
            for visit_m in m[::-1]:
                result.append(matrix[visit_m][visit_n])
            if len(result) >= len(matrix)*len(matrix[0]):
                break
            else:
                del n[0]
            print(result,m,n)
    
        return result
    
        # --- Better Solution ---

    

# --- TEST ---

# Expected: [1,2,3,6,9,8,7,4,5]
matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
# Expected: [1,2,3,4,8,12,11,10,9,5,6,7]
matrix2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

s = Solution()
print(s.spiralOrder(matrix1))
print(s.spiralOrder(matrix2))