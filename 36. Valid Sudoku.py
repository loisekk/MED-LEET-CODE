class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # a bit reference for an F1 fan "box_box"

        row = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        box_box = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                value = board[r][c]

                if value == ".":
                 continue 
            
                box_id = (r//3) * 3 + (c // 3)

                if (value   in row[r] or value in  cols[c] or value in box_box[box_id]):
                 return False

                row[r].add(value) 
                cols[c].add(value) 
                box_box[box_id].add(value) 

        return True 