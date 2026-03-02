class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        s_ip = []
        
        def backtrack(start , path):
            if len(path) == 4:
                if start == len(s):
                    s_ip.append('.'.join(path))
                return

            for length in range(1 , 4):
                if start + length > len(s):
                    break
                p = s[start:start + length]
                
                if len(p) > 1 and p[0] == '0':
                    continue
                if int(p) <= 255:
                    backtrack(start + length ,path + [p])
        backtrack(0 , [])
        return s_ip