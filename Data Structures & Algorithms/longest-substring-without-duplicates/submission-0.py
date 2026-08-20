class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()

        left = 0
        max_lenght = 0

        for right in range(len(s)):

            while s[right] in window:
                window.remove(s[left])
                left += 1

            window.add(s[right])
            
            max_lenght = max(max_lenght, right - left + 1)

        return max_lenght
        