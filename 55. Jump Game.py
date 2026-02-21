class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_jump = 0

        for i in range(len(nums)):
            if i > max_jump :
                return False
            max_jump = max(max_jump , i +nums[i])
        return True 