'''
713. 乘积小于k的子数组
给定一个正整数数组 nums和整数 k 。请找出该数组内乘积小于 k 的连续的子数组的个数。
示例 1:
输入: nums = [10,5,2,6], k = 100
输出: 8
解释: 8 个乘积小于 100 的子数组分别为: [10], [5], [2], [6], [10,5], [5,2], [2,6], [5,2,6]。需要注意的是 [10,5,2] 并不是乘积小于 100 的子数组。
示例 2:
输入: nums = [1,2,3], k = 0
输出: 0
提示:   1 <= nums.length <= 3 * 10^4
1 <= nums[i] <= 1000
0 <= k <= 10^6  
'''

class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        ans = 0
        sum_= 1
        i = 0
        for j,num in enumerate(nums):
            sum_ *= num
            while i<=j and sum_ >= k:
                sum_ //= nums[i]
                i += 1
            ans += j - i + 1
        return ans
    
if __name__ == "__main__":
    nums = [10,5,2,6]
    k = 100
    solution = Solution()
    result = solution.numSubarrayProductLessThanK(nums,k)
    print(result)