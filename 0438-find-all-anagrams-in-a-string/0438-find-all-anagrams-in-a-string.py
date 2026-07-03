from collections import Counter
class Solution(object):
    def findAnagrams(self, s, p):
        low = 0 
        k = len(p)
        freq_p = Counter(p)
        freq_s = {}
        res = []
        if len(p) > len(s) :
            return res
        for i in range(k) :
            freq_s[s[i]] = freq_s.get(s[i], 0) + 1
        if freq_s == freq_p :
            res.append(0)
        for high in range(k, len(s)) :
            freq_s[s[high]] = freq_s.get(s[high],0) + 1
            freq_s[s[low]] -= 1
            if freq_s[s[low]] == 0 :
                del freq_s[s[low]]
            low += 1
            if freq_p == freq_s :
                res.append(low)
        return res
            
