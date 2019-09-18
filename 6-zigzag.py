class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if (numRows == 1) or (numRows>=len(s)):
            return s
        
        # contruct a grid for zigzag
        grid = ['' for i in range(numRows)]

        row , step = 0, 1


        for c in s:
            # put tht char behind the corresponding row
            grid[row] += c

            # reach row 0: begin with row 1
            if row == 0:
                step = 1
            elif row == numRows-1:
                # when reach last row, go back to the second last row
                step =-1
            # update row info
            row = row+step
        return ''.join(grid)
