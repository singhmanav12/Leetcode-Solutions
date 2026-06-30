class Solution(object):
    def maxConsecutiveAnswers(self, answerKey, k):
        low = 0 
        res = 0
        freq_T = 0
        freq_F = 0
        for high in range(len(answerKey)) :
            if answerKey[high] == 'T' :
                freq_T += 1
            elif answerKey[high]  == 'F' :
                freq_F += 1
            while min(freq_T, freq_F) > k :
                if answerKey[low] == 'T' :
                    freq_T -= 1
                else :
                    freq_F -= 1
                low += 1
            res = max(res, high - low + 1)
        return res
                    
