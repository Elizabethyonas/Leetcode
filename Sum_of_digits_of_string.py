class Solution:
    def getLucky(self, s: str, k: int) -> int:
        def operation(si):
            ans = 0
            for chr in si:
                ans += int(chr)
            return ans

        lowercase_letters = string.ascii_lowercase
        letter_index = ''
        for chr in s:
            letter_index += str(lowercase_letters.index(chr) + 1)
        while k > 0:
            temp = operation(letter_index)
            letter_index = str(temp)
            k -= 1
        return int(letter_index)
