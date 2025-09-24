

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        res = 0
        j = -1
        for i in range(len(s)):
            if s[i] in dic:     #若之前遇到过，则更新最大位置
                j = max(dic[s[i]] , j)
            dic[s[i]] = i
            res = max(res,i - j)
        return res
    
if __name__ == "__main__":
    s = "abba"
    solution = Solution()
    result = solution.lengthOfLongestSubstring(s)
    print(result)