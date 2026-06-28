class Solution(object):
    def reverseWords(self, s):
        w = s.split()
        for i in range(len(w)) :
            w[i]=w[i][::-1]


        return " ".join(w)