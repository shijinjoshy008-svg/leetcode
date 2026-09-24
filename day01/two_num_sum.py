nums = [1,2,3,4,5,6]
target = 5
for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    print(i,j)
        # Return an empty list if no solution is found
print()