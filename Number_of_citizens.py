class Solution:
    def countSeniors(self, details: List[str]) -> int:
        old = 0
        for i in range(len(details)):
            curr = int(details[i][11] + details[i][12])
            if curr > 60:
                old += 1
        return old
