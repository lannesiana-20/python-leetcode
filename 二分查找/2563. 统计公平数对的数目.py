class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        nums.sort()
        def count(x):
            cnt = 0 
            j = n - 1
            for i in range(n):
                while j > i and nums[i] + nums[j] > x:
                    j -= 1  #右移左指针
                if j <= i:
                    break
                cnt += j - i
            return cnt

        return count(upper) - count(lower - 1)