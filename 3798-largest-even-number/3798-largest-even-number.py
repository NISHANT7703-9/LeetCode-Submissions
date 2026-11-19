class Solution:
    def largestEven(self, s: str) -> str:

        last = -1

        for i in range(len(s)):
            if s[i] == '2':
                last = i

        if last == -1:
            return ""

        return s[:last+1]
        