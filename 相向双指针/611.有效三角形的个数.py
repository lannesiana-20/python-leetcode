'''
611. 有效三角形的个数
给定一个包含非负整数的数组，你的任务是统计其中可以组成三角形的三元组个数。
示例 1:
输入: [2,2,3,4]
输出: 3
解释:有效的组合是:  
2,3,4 (使用第一个 2)
2,3,4 (使用第二个 2)
2,2,3
示例 2: 
输入: [4,2,3,4]
输出: 4
'''


class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums = sorted(nums)
        ans = 0
        for k in range(2,n):
            c = nums[k]     #c表示第三边，首先固定第三边
            i = 0
            j = k-1
            while i < j:
                if nums[i] + nums[j] > c:
                    ans += j - i
                    j -= 1
                else:
                    i += 1
        return ans