class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        low = 0 
        current_cost = 0 
        res = 0
        for high in range(len(s)) :
            cost = abs(ord(s[high]) - ord(t[high]))
            current_cost = current_cost + cost
            while current_cost > maxCost :
                current_cost = current_cost - abs(ord(s[low]) - ord(t[low]))
                low += 1
            res = max(res, high - low + 1)
        return res