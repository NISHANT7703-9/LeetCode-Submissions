class Solution:
    def maxArea(self, height: list[int]) -> int:
        i=0
        j=len(height)-1
        area=0
        maximum=0
        while j>i:
            
            a=min(height[i],height[j])
            b=j-i
            area=a*b
            maximum=max(maximum,area)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return maximum
            

        