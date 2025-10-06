'''
1234. 替换子串得到平衡字符串
中等
1.3K    相关标签            
premium lock icon
相关企业
有一个只含有 'Q', 'W', 'E', 'R' 四种
字符的字符串 s 。如果一个字符串中 'Q', 'W', 'E', 'R' 四种字符都恰好出现 n/4 次（n 是该字符串的长度），则认为这个字符串是 平衡 的。          
给你一个平衡字符串 s ，请你返回将 s 替换成平衡字符串所需要替换的最小子串的长度。
如果原字符串就是平衡的，则返回 0。
示例 1：
输入：s = "QWER"
输出：0
解释：s 已经是平衡的了。
示例 2：
输入：s = "QQWE"
输出：1
'''

class Solution:
    def balancedString(self, s: str) -> int:
        time = len(s) // 4
        cnt = Counter(s)
        if len(cnt) == 4 and min(cnt.values()) == time:
            return 0    #不需要替换任何
        # 右指针负责扩大滑窗，左指针负责缩小滑窗
        ans, left = inf, 0 
        for right , c in enumerate(s):
            cnt[c] -= 1 
            while max(cnt.values()) <= time:    #满足要维护的滑窗要求——所有字符计数小于等于次数len/4
                ans = min(ans, right - left + 1)
                cnt[s[left]] += 1   #尝试缩小滑窗大小，先让滑窗外的cnt计数+1,再右移左指针
                left += 1

        return ans