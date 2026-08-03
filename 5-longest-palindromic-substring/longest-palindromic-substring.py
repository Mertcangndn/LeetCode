class Solution:

    def longestPalindrome(self, s: str) -> str:
        result = ""

        for left in range(len(s)):
            for right in range(len(s) - 1, left - 1, -1):
                if (right - left + 1) <= len(result):
                    break

                current = s[left : right + 1]
                
                if current == current[::-1]:
                    result = current
                    break

        return result