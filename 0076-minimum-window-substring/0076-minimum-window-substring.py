from collections import Counter 
class Solution(object):
    def minWindow(self, s, t):
        low = 0 
        res = [-1,-1]
        res_len = float('inf')
        freq_t = Counter(t)
        need = len(freq_t)
        have = 0
        freq_s = {}
        if len(t) > len(s) :
            return ""
        for high in range(len(s)) :
            if s[high] in freq_t :
                freq_s[s[high]] = freq_s.get(s[high], 0) + 1
                if freq_s[s[high]] == freq_t[s[high]] :
                    have += 1
            while need == have :
                window_length = high - low + 1
                if window_length < res_len :
                    res = [low,high]
                    res_len = window_length
                if s[low] in freq_t :
                    freq_s[s[low]] -= 1
                    if freq_s[s[low]] < freq_t[s[low]] :
                        have -= 1
                low += 1
        left, right = res
        if res_len != float('inf') :
            return s[left : right + 1]
        return ""


        