class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ch = set()
        left = 0
        maxx = 0
        for r in range(len(s)):
            while s[r] in ch :
                ch.remove(s[left] )
                left += 1
            ch.add(s[r])
            maxx = max(maxx , r - left + 1 )
        return maxx
            