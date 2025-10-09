class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n , m = len(spells), len(potions)
        #排序
        potions.sort()
        ans = []
        '''思路：对potions进行内部升序排序，从最小那个数开始遍历，如果和spells相乘已经大于等于success，则后面都不用计算了，直接算后面还有几个数就行'''
        for i in range(n):
            x = spells[i]
            cnt = 0
            left, right = 0,m-1
            while left < right:
                mid = (left + right) // 2
                if potions[mid] * x >= success:
                    right = mid
                else:
                    left = mid + 1
            if potions[left] * x >= success:
                cnt = m - left
            ans.append(cnt)
        return ans