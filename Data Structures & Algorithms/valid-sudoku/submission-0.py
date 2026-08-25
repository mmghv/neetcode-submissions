class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sCols = [set() for _ in range(9)]
        sSubgrids = [set() for _ in range(9)]

        for ir in range(9):
            sRow = set()
            for ic in range(9):
                cell = board[ir][ic]
                if cell == '.': continue
                isg = (ir // 3) + ((ic // 3) * 3)
                if cell in sRow: return False
                if cell in sCols[ic]: return False
                if cell in sSubgrids[isg]: return False
                sRow.add(cell)
                sCols[ic].add(cell)
                sSubgrids[isg].add(cell)
        return True

