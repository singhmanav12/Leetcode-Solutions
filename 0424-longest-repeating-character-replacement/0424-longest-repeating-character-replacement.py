class Solution(object):
    def characterReplacement(self, s, k):
        low = 0
        res  =0
        freq ={}
        max_freq = 0 
        for high in range(len(s)) :
            freq[s[high]] = freq.get(s[high],0) + 1
            length = high - low + 1
            max_freq = max(max_freq, freq[s[high]])
            while length - max_freq > k :
                freq[s[low]] -= 1
                low += 1
                length = high - low + 1
            res = max(res, length)
        return res
        