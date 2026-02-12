class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        results = []

        def backtrack(start , path , remaining):
            if remaining == 0:
              results.append(path[:])
              return 
            if remaining < 0:
                return 
            for i in range(start , len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > remaining :
                    break

                path.append(candidates[i])
                backtrack(i+1 , path ,remaining - candidates[i])

                path.pop()
        backtrack(0 ,[] , target)
        return results 
                
