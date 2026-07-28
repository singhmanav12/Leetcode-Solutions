class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i=0
        j=0
        list=[]
        while i<m and j<n :
            if nums1[i] < nums2[j] :
                list.append(nums1[i])
                i+=1
            else :
                list.append(nums2[j])
                j+=1
        while i<m :
            list.append(nums1[i])
            i+=1
        while j<n :
            list.append(nums2[j])
            j+=1
        for k in range(m+n) :
            nums1[k] = list[k]
        print(nums1)