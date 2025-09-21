'''
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。
'''

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        if not nums or n < 3:
            return []
        nums.sort() # 排序
        res = []
        for i in range(n):
            if nums[i] > 0:     #用于判断第一个数，若第一个数为正则直接返回
                return res
            if i > 0 and nums[i] == nums[i-1]:  #前后两个数相等则往下循环，避免输出重复组合
                continue
            L = i+1
            R = n-1
            while L < R:
                if nums[i] +nums[L] +nums[R] == 0:
                    res.append([nums[i],nums[L],nums[R]])
                    # 若中途又遇见左指针和下一个会重复，则多右移一位
                    while L < R and nums[L] == nums[L+1]:
                        L += 1
                    # 若右指针左移的下一位会重复，则多左移一位
                    while L < R and nums[R] == nums[R-1]:
                        R -= 1
                    L += 1
                    R -= 1
                # 若sum大了，则右指针左移
                elif nums[i]+nums[L]+nums[R] > 0:
                    R -= 1
                # 若sum小了，则左指针右移
                else:
                    L += 1
        return res


