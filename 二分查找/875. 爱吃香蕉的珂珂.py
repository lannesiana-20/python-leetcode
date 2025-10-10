class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)  # 右边界：最大的那堆香蕉数
        
        while left < right:
            mid = left + (right - left) // 2  # 防止溢出
            total_h = 0
            for pile in piles:
                total_h += math.ceil(pile / mid)  # 计算每堆需要的时间，向上取整
            if total_h <= h:
                right = mid  # 当前k可行，尝试更小的k
            else:
                left = mid + 1  # 当前k太小，需要更大的k
        return left