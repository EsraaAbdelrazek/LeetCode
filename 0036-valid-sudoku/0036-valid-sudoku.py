class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Use sets
        Col = [set() for _ in range(9)]
        Row = [set() for _ in range(9)]
        Block = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                c=board[i][j]
                if c=='.': continue
                x=(ord(c)-ord('0'))%9

                if x in Row[i]: return False
                Row[i].add(x)

                if x in Col[j]: return False
                Col[j].add(x)

                idx=i//3*3+j//3
                if x in Block[idx]: return False
                Block[idx].add(x)
        return True