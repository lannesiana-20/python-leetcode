'''
给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。

找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

返回容器可以储存的最大水量。

说明：你不能倾斜容器。
'''
'''
思路：每次移动的是较短的那一边，因为移动较长的那一边不可能获得更大的面积
'''
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i , j, res = 0, len(height)-1,0
        while i < j:      #左右指针相遇时跳出即可
            # 左边板短于右边板
            if height[i] < height[j]:
                res = max(res,height[i]*(j-i))
                i += 1  #谁矮谁移动
            else:
                res = max(res,height[j]*(j-i))
                j -= 1
        return res