class Solution:
    def canAliceWin(self, n: int) -> bool:

        stones = 10
        Alice = 1
        Bob = 0

        while n >= stones:
            n -= stones
            stones -= 1

            if Alice == 1:
                Alice = 0
                Bob = 1
            else:
                Alice = 1
                Bob = 0

        return Bob == 1
        