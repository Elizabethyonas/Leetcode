class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count_steps(prefix, n):
            steps = 0
            first = prefix
            next = prefix + 1
            while first <= n:
                steps += min(n + 1, next) - first
                first *= 10
                next *= 10
            return steps

        curr = 1
        k -= 1  # Start from 1, so reduce k by 1

        while k > 0:
            steps = count_steps(curr, n)
            if steps <= k:
                # Move to the next prefix
                curr += 1
                k -= steps
            else:
                # Go deeper into the current prefix
                curr *= 10
                k -= 1

        return curr
