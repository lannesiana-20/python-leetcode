class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ans = left = 0
        cnt = defaultdict(int)
        for right,x in enumerate(nums):  #right是右指针的index,x是对应index的具体取值
            cnt[x] += 1
            while cnt[x] > k:
                cnt[nums[left]] -= 1
                left += 1   #右移zuozhizhen
            ans = max(ans, right - left + 1)
        return ans