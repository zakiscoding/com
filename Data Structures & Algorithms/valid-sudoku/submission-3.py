class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen=set()
        for r in range(len(board)):
            for c in range(len(board)):
                num  = board[r][c]
                if num==".":
                    continue
                row_key=('row', r, num)
                col_key=('col', c, num)
                box_key=('box', r//3, c//3, num)

                if box_key in seen or row_key in seen or col_key in seen:
                    return False

                seen.add(row_key)
                seen.add(col_key)
                seen.add(box_key)
        return True
