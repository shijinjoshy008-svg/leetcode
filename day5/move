class Solution(object):
    def moveZeroes(self, nums):

        pos = 0

        # Move non-zero elements to the front
        for i in range(len(nums)):

            if nums[i] != 0:
                nums[pos] = nums[i]
                pos += 1

        # Fill remaining positions with zero
        while pos < len(nums):
            nums[pos] = 0
            pos += 1