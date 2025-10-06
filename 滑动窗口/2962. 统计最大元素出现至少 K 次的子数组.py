'''

代码
测试用例
测试结果
测试结果
2962. 统计最大元素出现至少 K 次的子数组
已解答
中等
相关标签
premium lock icon
相关企业
给你一个整数数组 nums 和一个 正整数 k 。

请你统计有多少满足 「 nums 中的 最大 元素」至少出现 k 次的子数组，并返回满足这一条件的子数组的数目。

子数组是数组中的一个连续元素序列。

 

示例 1：

输入：nums = [1,3,2,3,3], k = 2
输出：6
解释：包含元素 3 至少 2 次的子数组为：[1,3,2,3]、[1,3,2,3,3]、[3,2,3]、[3,2,3,3]、[2,3,3] 和 [3,3] 。
示例 2：

输入：nums = [1,4,2,1], k = 3
输出：0
解释：没有子数组包含元素 4 至少 3 次。
'''


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l = 0
        ans = 0
        cnt = 0
        max_num = max(nums)
        for x in nums:
            if x == max_num:
                cnt += 1
            while cnt == k:  # 维护区间窗口保持最大值的数目一直小于k
                if nums[l] == max_num:
                    cnt -= 1
                l += 1   
            ans += l   #那么left指针左手边的所有区间则都满足
        return ans