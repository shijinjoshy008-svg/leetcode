
# Reverse String 

class Solution:
    def reverseString(self, s):

        left = 0
        right = len(s) - 1

        while left < right:

            temp = s[left]
            s[left] = s[right]
            s[right] = temp

            left = left + 1
            right = right - 1



s = ["h","i"]

obj = Solution()
obj.reverseString(s)

print(s)