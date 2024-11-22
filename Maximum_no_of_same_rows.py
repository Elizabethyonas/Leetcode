class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        ans = 0

        for current_row in matrix:
            flipped_row = [1 - cell for cell in current_row]

            equivalent_row = 0
            for potential_row in matrix:
                if potential_row == current_row or potential_row == flipped_row:
                    equivalent_row += 1
            
            ans = max(ans, equivalent_row)
        return ans
