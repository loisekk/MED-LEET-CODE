class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        def dfs(index , path , total):
              if total == target:
                result.append(path[:])
                return 

              if total > target or index >= len(candidates):
                return 

              path.append(candidates[index])
              dfs(index , path , total + candidates[index])

              path.pop()

              dfs(index + 1 , path , total)

        dfs(0 , [] ,0)
        return result
              
            