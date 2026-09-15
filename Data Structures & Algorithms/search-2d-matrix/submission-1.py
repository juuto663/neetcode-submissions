from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        left_bound, right_bound = 0, (rows * cols) - 1

        while left_bound <= right_bound:
            median = (left_bound + right_bound) // 2
            mid_r, mid_c = self.convert_to_coordinate(pos=median, num_cols=cols)
            print(f"{mid_r} and {mid_c}")
            search_val = matrix[mid_r][mid_c]

            if search_val > target:
                right_bound = median - 1
            elif search_val < target:
                left_bound = median + 1
            else:
                return True

        return False

    def convert_to_coordinate(self, pos: int, num_cols: int) -> tuple:
        row = pos // num_cols
        col = pos % num_cols
        return (row, col)