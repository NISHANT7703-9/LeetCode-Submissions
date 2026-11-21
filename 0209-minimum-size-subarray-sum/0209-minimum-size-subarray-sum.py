class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:

        i = 0
        s = 0
        ans = float('inf')

        for j in range(len(nums)):
            s += nums[j]

            while s >= target:
                ans = min(ans, j - i + 1)
                s -= nums[i]
                i += 1

        if ans == float('inf'):
            return 0

        return ans

        