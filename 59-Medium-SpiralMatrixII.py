class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        # --- My Solution ---
        num = n*n

        result = [[0 for _ in range(n)] for _ in range(n)]

        m = [i for i in range(n)]
        n = [i for i in range(n)]

        visit_m = 0
        visit_n = 0

        count = 1

        while True:

            # Visit right
            for visit_n in n:
                result[visit_m][visit_n] = count
                count += 1
            if count > num:
                break
            else:
                del m[0]
            
            # Visit down
            for visit_m in m:
                result[visit_m][visit_n] = count
                count += 1
            if count > num:
                break
            else:
                del n[-1]
            
            # Visit left
            for visit_n in n[::-1]:
                result[visit_m][visit_n] = count
                count += 1
            if count > num:
                break
            else:
                del m[-1]
            
            # Visit up
            for visit_m in m[::-1]:
                result[visit_m][visit_n] = count
                count += 1
            if count > num:
                break
            else:
                del n[0]

        return result

    
        # --- Better Solution ---
    

# --- TEST ---

# Expected: [[1,2,3],[8,9,4],[7,6,5]]
matrix1 = 3
# Expected: [[1]]
matrix2 = 1

s = Solution()
print(s.generateMatrix(matrix1))
print(s.generateMatrix(matrix2))