'''
给你一个整数数组 nums 和一个整数 x 。每一次操作时，你应当移除数组 nums 最左边或最右边的元素，然后从 x 中减去该元素的值。请注意，需要 修改 x 的值，而不是 数组 nums 。
请你返回将 x 减到 0 的 最小操作数 ，如果无法减到 0 ，则返回 -1 。
子数组 是数组的 连续 部分。
示例 1：
输入：nums = [1,1,4,2,3], x = 5
输出：2
解释：最佳方案是移除后两个元素，2 和 3 ，共计
    2 次操作。
示例 2：
输入：nums = [5,6,7,8,9], x = 4
输出：-1
解释：无法移除元素减到 0 。
示例 3：
输入：nums = [3,2,20,1,1,3], x =
10
输出：5
解释：最佳方案是移除前 3 个元素和后 2 个元素，共计 5 次操作。
提示：
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^4
1 <= x <= 10^9
'''

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # 剩余子数组之和
        target = sum(nums) - x
        if target < 0 :
            return -1
        
        ans = -1
        cur_sum = left = 0
        for right , x in enumerate(nums):
            cur_sum += x
            while cur_sum > target:
                cur_sum -= nums[left]
                left += 1   #缩小子数组长度
            if cur_sum == target:
                ans = max(ans, right - left + 1)
        
        return -1 if ans < 0 else len(nums) - ans       #全部长度减去子区间长度，就是剩余需要移除的长度