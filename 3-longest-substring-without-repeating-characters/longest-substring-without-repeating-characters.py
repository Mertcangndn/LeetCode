class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        kume = set()
        left = 0
        result = 0

        for right in range(len(s)):
            while s[right] in kume:
                kume.remove(s[left])
                left += 1

            kume.add(s[right])
            result = max(result, right - left + 1)

        return result