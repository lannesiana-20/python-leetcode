'''
给你一个长度为 n 的整数数组 nums 和 一个目标值 target。请你从 nums 中选出三个整数，使它们的和与 target 最接近。
返回这三个数的和。
假定每组输入只存在恰好一个解。
'''
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        """
        用到三个指针，
        第一个：i确定首位，依次往右移动
        第二个：j = i+1，往右移动
        第三个：k = len - 1,从右往左移动

        若sum > target , k左移，反之，j右移
        """ 
        nums.sort()     # 升序排序
        n, ans = len(nums), nums[0] + nums[1] + nums[2]
        for i in range(n):
            # 减少运行次数，因为如果后一个和前一个的数值相同，相当于前一个已经提前运行过一遍了，不必再次运行
            if i >=1 and nums[i] == nums[i-1]:
                continue
            j,k = i + 1, n - 1
            while j < k:
                # 当前三数之和
                current_sum = nums[i] + nums[j] + nums[k]
                if abs(current_sum - target) < abs(ans - target):
                    ans = current_sum
                if ans == target:
                    return target
                elif current_sum > target:
                    k -= 1
                elif current_sum < target:
                    j += 1
        
        return ans