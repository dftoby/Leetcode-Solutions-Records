class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        
        # --- My Solution ---
        '''
        [1, 2, 3, 4]
        [5, 6, 7, 8]
        [9,10,11,12]
        '''
        result = []
        # UP:   [0,0]
        # DOWN: [0,1],[1,0]
        # UP:   [2,0],[1,1],[0,2]
        # DOWN: [0,3],[1,2],[2,1]
        # UP:   [2,2],[1,3]
        # DOWN: [2,3]

        m = len(mat)
        n = len(mat[0])

        visit_m = 2
        visit_n = 0

        while True:

            # Up
            for 




        return result

        # --- Better Solution ---

    

# --- TEST ---
# Expected: [1,2,4,7,5,3,6,8,9]
matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
# Expected: [1,2,3,4]
matrix2 = [[1,2],[3,4]]

s = Solution()
print(s.findDiagonalOrder(matrix1))
print(s.findDiagonalOrder(matrix2))