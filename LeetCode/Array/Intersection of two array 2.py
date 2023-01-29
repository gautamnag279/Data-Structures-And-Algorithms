class Solution:
    def intersect(self, nums1, nums2):
        a, b = map(collections.Counter, (nums1, nums2))
        return list((a & b).elements()) #.elements() is an attribute of the counter module
    
