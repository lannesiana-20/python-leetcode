'''
二分查找关键点：看是否存在「单调非递减」关系
'''
class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left = 1
        # 右边界：最快的公交车跑totalTrips趟的时间，因为题目要求的是花费的「最少」时间
        right = min(time) * totalTrips
        #左右双指针分别指向花费的总时间
        while left < right:
            mid = (left + right) // 2
            total = 0
            for t in time:
                total += mid // t  # 每辆车在mid时间内的「趟数」    
            if total >= totalTrips:
                # 时间足够，尝试更小的时间
                right = mid
            else:
                # 时间不足，需要更大的时间
                left = mid + 1
        return left