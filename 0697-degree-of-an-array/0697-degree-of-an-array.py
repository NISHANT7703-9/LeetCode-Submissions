class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:

        d = {}
        first = {}
        last = {}

        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]] += 1
            else:
                d[nums[i]] = 1
                first[nums[i]] = i

            last[nums[i]] = i

        degree = max(d.values())
        ans = len(nums)

        for i in d:
            if d[i] == degree:
                length = last[i] - first[i] + 1

                if length < ans:
                    ans = length

        return ans
        