class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        n1 , n2 , n3 = len(s1) , len(s2) , len(s3)
        
        if n1 + n2 != n3:
            return False
        dp = [[False] * (n2 + 1) for _ in range(n1 + 1)]
        dp[0][0] = True
        
        for i in range(n1 + 1):
            for j in range(n2 + 1):
                if i > 0:
                    dp[i][j] = dp[i][j] or (
                        dp[i-1][j] and s1[i-1] == s3[i+j-1]
                    )
                
                if j > 0:
                    dp[i][j] = dp[i][j] or (
                        dp[i][j-1] and s2[j-1] == s3[i+j-1]
                    )
        
        return dp[n1][n2]