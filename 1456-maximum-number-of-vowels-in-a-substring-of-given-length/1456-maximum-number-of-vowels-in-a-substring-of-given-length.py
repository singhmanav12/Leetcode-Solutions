class Solution(object):
    def maxVowels(self, s, k):
        low = 0
        vowels = set("aeiou")
        vowel_count = 0
        res = 0
        for i in range(k) :
            if s[i] in vowels :
                vowel_count += 1
        res = vowel_count
        for high in range(k, len(s)) :
            if s[high] in vowels :
                vowel_count += 1
            if s[low] in vowels :
                vowel_count -= 1
            low += 1
            res = max(vowel_count, res)
        return res
        
        