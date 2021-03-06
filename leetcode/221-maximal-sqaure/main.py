"""
    1st approach: classic dynamic programming approach
    - similar to lc1277

    ref:
    - https://www.youtube.com/watch?v=NYeVhmWsWec

    Time  O(r*c)
    Space O(r*c)
    160 ms, faster than 93.75%
"""


class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        r, c = len(matrix), len(matrix[0])
        dp = [c * [0] for _ in range(r)]
        result = 0
        # for each cell, check if itself can complete a larger square
        for i in range(r):
            for j in range(c):
                if i == 0 or j == 0:
                    dp[i][j] = int(matrix[i][j])
                elif matrix[i][j] == '1':
                    # the current grid = 1min among upperleft, left, up + 1
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                result = max(result, dp[i][j])
        # area of a square
        return result*result


a = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"],
]
print(Solution().maximalSquare(a))

a = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "0", "0"],
]
print(Solution().maximalSquare(a))
