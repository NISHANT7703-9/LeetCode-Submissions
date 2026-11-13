Problem: Two Sum

LeetCode: 1

Difficulty: Easy

Topic: Array

Language: Python

Approach: Brute Force

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return (i,j)
                else:
                    pass
    
        return()

Time Complexity: O(n²)

Space Complexity: O(1)
