class Solution(object):
    def majorityElement(self, nums):
        candidate = None
        count = 0
        
        for value in nums:
            
            if count == 0:
                
                candidate = value
                
                count += 1 if value == candidate else -1
                
                return candidate