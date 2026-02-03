class Solution:
    def longestString(self, x, y, z):
        
        
      return (min(x,y)*2 + ( 1 if x != y else 0 ) + z ) * 2
