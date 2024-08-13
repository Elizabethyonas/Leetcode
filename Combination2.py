class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        def combination_sum(temp, idx, curr_sum):
            if curr_sum > target :
                return 
            if curr_sum == target :
                ans.append(temp.copy())
                return
            if idx >= len(candidates):
                return
            temp.append(candidates[idx])
            combination_sum(temp, idx + 1, curr_sum + candidates[idx])
            temp.pop()
            curr = candidates[idx]
            while idx < len(candidates) and curr == candidates[idx]:
                idx += 1
            combination_sum(temp, idx, curr_sum)
        combination_sum([], 0, 0)
        return ans
