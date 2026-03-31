class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for num in range(9):
            # Check row
            set_num = set()
            for val in board[num]:
                if val == ".":
                    continue
                if val in set_num:
                    return False
                set_num.add(val)
            # Check column
            set_num = set()
            for row in range(9):
                cur = board[row][num]
                if cur == ".":
                    continue
                if cur in set_num:
                    return False
                set_num.add(cur)
        # Check subgrid
        for col in range(0,9,3):
            for row in range(0,9,3):
                set_num = set()
                for col_adj in range(3):
                    for row_adj in range(3):
                        cur = board[col+col_adj][row+row_adj]
                        if cur == ".":
                            continue
                        if cur in set_num:
                            return False
                        set_num.add(cur)
        return True