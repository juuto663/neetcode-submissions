class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sub_matrix = collections.defaultdict(set)
        row = collections.defaultdict(set)
        col = collections.defaultdict(set)

        num_row = len(board)
        num_col = len(board[0])

        for i in range(num_row):
            for j in range(num_col):
                num = board[i][j]
                if num == ".":
                    continue
                # Submatrix
                sub_r, sub_c = i // (num_row / 3), j // (num_col / 3)
                if num in sub_matrix[(sub_r, sub_c)]:
                    return False
                else:
                    sub_matrix[(sub_r, sub_c)].add(num)
                
                # Row
                if num in row[i]:
                    return False
                else:
                    row[i].add(num)
                # Col
                if num in col[j]:
                    return False
                else:
                    col[j].add(num)

        return True