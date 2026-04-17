class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        start, end = 0, 0

        maxfreq = 0
 
        for end, char in enumerate(s):
            count[char] = count.get(char, 0) + 1

            if count[char] > maxfreq:
                maxfreq = count[char]
            
            if end - start + 1 - maxfreq > k:
                count[s[start]] -= 1
                start += 1
            
        return end - start + 1
