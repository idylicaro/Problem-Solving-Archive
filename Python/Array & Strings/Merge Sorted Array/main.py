# The problem is:
## You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
## Merge nums1 and nums2 into a single array sorted in non-decreasing order.
## The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

### ref: https://leetcode.com/problems/merge-sorted-array/description

def merge(nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        # This not need because if m = 0, nums1 is empty and enter into second while.
        #if n == 0:
        #    return nums1
        #elif m == 0 and n > 0: 
        #    return nums2
        
        x = m - 1
        y = n - 1
        z = m + n - 1 # the last position in nums1 array

        while x >= 0 and y >= 0:
            # compare the last position of nums1 and last position of nums2 and put in z position.
            if nums1[x] > nums2[y]:
                nums1[z] = nums1[x]
                nums1[x] = 0
                x-=1
            else:
                nums1[z] = nums2[y]
                y-=1

            z-=1
        
        # When position before x is empty. Put all y positions in the rest of array.
        while y >= 0:
            nums1[z] = nums2[y]
            y -= 1
            z -= 1
        
        return nums1