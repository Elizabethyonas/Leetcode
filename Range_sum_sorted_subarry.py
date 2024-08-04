class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        subs = []
        MOD = 10 ** 9 + 7

        for i in range(n):
            curr = 0
            for j in range(i, n):
                curr += nums[j]
                subs.append(curr)

        subs.sort()

        return sum(subs[left-1:right]) % MOD
