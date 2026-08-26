# bitwise
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [0] * 9
        subgrids = [0] * 9

        for r in range(9):
            row = 0
            for c in range(9):
                cell = board[r][c]
                if cell == '.': continue
                mask = 1 << (int(cell) - 1)
                sg = (r // 3) + ((c // 3) * 3)
                if row & mask or cols[c] & mask or subgrids[sg] & mask:
                    return False
                row |= mask
                cols[c] |= mask
                subgrids[sg] |= mask
        return True

