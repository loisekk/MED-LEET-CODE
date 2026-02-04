class Solution(object):
    def numberOfArrays(self, differences, lower, upper):
        """
        :type differences: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        curr = 0
        minSum = 0
        maxSum = 0

        for d in differences:
            curr += d
            minSum = min(minSum, curr)
            maxSum = max(maxSum, curr)

        return max(0, (upper - maxSum) - (lower - minSum) + 1)
        