class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for i in range(9):
            for j in range(9):
                cur = board[i][j]
                if cur == '.':
                    continue
                if cur in rows[i]:
                    return False
                rows[i].add(cur)
                if cur in cols[j]:
                    return False
                cols[j].add(cur)
                if cur in boxes[(i//3,j//3)]:
                    return False
                boxes[(i//3,j//3)].add(cur)
        return True
