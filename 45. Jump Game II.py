class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        jump = 0
        farthest = 0 
        end = 0 
        
        
        for i in range(len(nums) -1):
            farthest = max(farthest , i + nums[i])
            if i == end:
                jump +=1 
                end = farthest
        return jump