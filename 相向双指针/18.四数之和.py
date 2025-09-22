'''
18. 四数之和
给你一个由 n 个整数组成的数组 nums ，和一个目标值 target
，请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[b], nums[c], nums[d]] ：
0 <= a, b, c, d < n
a、b、c 和 d 互不相同
nums[a] + nums[b] + nums[c] + nums[d] == target
你可以按 任意顺序 返回答案 。
'''

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        n,ans = len(nums), []
        for a in range(n-3):
            # 枚举第一个数，遍历后面3个数
            x = nums[a]
            # 先判断完所有需要continue的条件
            if a and x == nums[a-1]:
                continue
            if x + nums[a+1] + nums[a+2] + nums[a+3] > target:
                break       #后面不可能有结果
            if x + nums[-3] + nums[-2] + nums[-1] < target:
                continue    #当前a能有的最大和
            # 第二层循环，枚举第二个数
            for b in range(a+1 , n-2):
                y = nums[b]
                # 跳过重复数
                if b > a+1 and y == nums[b-1]:
                    continue
                if x + y + nums[b+1] + nums[b+2] > target:
                    break
                if x + y +nums[-2] +nums[-1] < target:
                    continue
                
                # 用双指针枚举第三个和第四个数,这里可以参考之前的三数之和
                c = b + 1
                d = n - 1
                
                while c < d:
                    allsum = x + y + nums[c] + nums[d]
                    if allsum > target:
                        d -= 1
                    elif allsum < target:
                        c += 1
                    else:       #allsum = target
                        ans.append([x,y,nums[c],nums[d]])
                        c += 1
                        while c < d and nums[c] == nums[c-1]:
                            c += 1
                        d -= 1
                        while c < d and nums[d] == nums[d+1]:
                            d -= 1
        return ans