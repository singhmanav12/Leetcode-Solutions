from collections import Counter
class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2) :
            return False
        low = 0
        k = len(s1)
        freq_s1 = Counter(s1)
        freq_s2 = {}
        for i in range(len(s1)) :
            freq_s2[s2[i]] = freq_s2.get(s2[i],0) + 1
        if freq_s1 == freq_s2 :
            return True
        for high in range(k, len(s2)) :
            freq_s2[s2[high]] = freq_s2.get(s2[high],0) + 1
            freq_s2[s2[low]] -= 1
            if freq_s2[s2[low]] == 0 :
                del freq_s2[s2[low]]
            low += 1
            if freq_s1 == freq_s2 :
                return True
        return False





        