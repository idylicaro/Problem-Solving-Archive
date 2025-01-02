def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        target_need = {}

        for i, n in enumerate(nums):
            x = target - n
            if i is 0:
                target_need[x] = (x,i) # (target - n, index)
                continue