class Solution(object):
    def sortedSquares(self, nums):
        pos_list = []
        neg_list = []
        for i in range(len(nums)):
            if nums[i]<0 :
                neg_list.append(nums[i]*nums[i])
            else :
                pos_list.append(nums[i]*nums[i])

        neg_list.reverse()
        j=0
        k=0
        merge_list=[]
        while j<len(pos_list) and k<len(neg_list) :
            if pos_list[j]<neg_list[k] :
                merge_list.append(pos_list[j])
                j+=1
            else :
                merge_list.append(neg_list[k])
                k+=1
        while j<len(pos_list) :
            merge_list.append(pos_list[j])
            j+=1
        while k<len(neg_list) :
            merge_list.append(neg_list[k])
            k+=1
        return merge_list