'''
1004. 最大连续1的个数 III
已解答
中等
相关标签
premium lock icon
相关企业
提示
给定一个二进制数组 nums 和一个整数 k，假设最多可以翻转 k 个 0 ，则返回执行操作后 数组中连续 1 的最大个数 
示例 1：

输入：nums = [1,1,1,0,0,0,1,1,1,1,0], K = 2
输出：6
解释：[1,1,1,0,0,1,1,1,1,1,1]
粗体数字从 0 翻转到 1，最长的子数组长度为 6。
示例 2：

输入：nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
输出：10
解释：[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
粗体数字从 0 翻转到 1，最长的子数组长度为 10。
'''


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cnt_zero = 0
        ans = l = 0
        for r in range(n):    #遍历右指针r
            if nums[r] == 0:    #若遇到0，则计数+1
                cnt_zero += 1
            while cnt_zero > k:     #若窗口内0的数目大于能够翻转的数目k，则右移左指针
                if nums[l] == 0:    # 若左指针指向的是0，则先将计数0的变量-1再右移左指针
                    cnt_zero -= 1
                l += 1
            ans = max(ans , r - l + 1)

        return ans