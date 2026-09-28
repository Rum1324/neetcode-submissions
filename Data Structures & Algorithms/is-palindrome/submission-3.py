class Solution:
    def isPalindrome(self, s: str) -> bool:
        curated = ""
        for c in s:
            curated += c if c.isalnum() else ''

        l, r = 0, len(curated) - 1
        while l < r:
            if curated[l].lower() != curated[r].lower():
                return False
            l += 1
            r -= 1
        return True