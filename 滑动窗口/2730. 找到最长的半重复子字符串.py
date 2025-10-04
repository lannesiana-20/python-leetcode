class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        if len(s) < 2:
            return 1
        
        max_len = 0
        l = 0
        pair = 0
        for r in range(1,len(s)):
            if s[r] == s[r-1]:
                pair += 1   #相邻的两个一样，则对数+1
            
            while pair == 2:   #如果对数=2则需要减小窗口
                if s[l] == s[l+1]:  #while循环直到遇到重复pair
                    pair -= 1
                l += 1
            
            max_len = max(max_len, r - l + 1)
        return max_len