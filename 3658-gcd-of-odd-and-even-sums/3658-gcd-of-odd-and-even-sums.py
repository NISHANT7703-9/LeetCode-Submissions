import math
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sum2=n*n
        sum1=n*(n+1)
        return math.gcd(sum1,sum2)


        