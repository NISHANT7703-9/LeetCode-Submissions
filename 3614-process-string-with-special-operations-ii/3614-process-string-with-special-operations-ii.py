class Solution:
    def processStr(self, s: str, k: int) -> str:

        length = 0

        # First pass: Calculate final length
        for ch in s:

            if ch == '*':
                length = max(0, length - 1)

            elif ch == '#':
                length *= 2

            elif ch == '%':
                continue

            else:
                length += 1

        # Check whether k is valid
        if k >= length:
            return "."

        # Second pass: Reverse the operations
        for ch in reversed(s):

            if ch == '*':
                length += 1

            elif ch == '#':
                length //= 2

                if k >= length:
                    k -= length

            elif ch == '%':
                k = length - 1 - k

            else:
                length -= 1

                if k == length:
                    return ch

        return "."
        