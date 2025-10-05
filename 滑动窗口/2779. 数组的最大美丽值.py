'''
2779. 数组的最大美丽值
中等
相关标签
premium lock icon
相关企业
提示
给你一个下标从 0 开始的整数数组 nums 和一个 非负 整数 k 。

在一步操作中，你可以执行下述指令：

在范围 [0, nums.length - 1] 中选择一个 此前没有选过 的下标 i 。
将 nums[i] 替换为范围 [nums[i] - k, nums[i] + k] 内的任一整数。
数组的 美丽值 定义为数组中由相等元素组成的最长子序列的长度。

对数组 nums 执行上述操作任意次后，返回数组可能取得的 最大 美丽值。

注意：你 只 能对每个下标执行 一次 此操作。

数组的 子序列 定义是：经由原数组删除一些元素（也可能不删除）得到的一个新数组，且在此过程中剩余元素的顺序不发生改变。
'''
'''
思路：排序 + 滑动窗口
    1. 对数组进行排序
    2. 使用双指针维护一个滑动窗口，窗口内的元素满足 max - min <= 2 * k
    3. 计算窗口的最大长度，即为所求的最大美丽值
只有当 nums[r] - k <= nums[l] + k 时，窗口内的元素才能通过操作变为相等，即二者区间存在重叠部分
    4. 时间复杂度 O(n log n)（排序） + O(n)
    5. 空间复杂度 O(1)
'''

class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        res, l, n = 0, 0, len(nums)
        nums.sort()
        for r in range(n):
            while nums[r] - k > nums[l] + k:
                l += 1
            res = max(res, r - l + 1)

        return res