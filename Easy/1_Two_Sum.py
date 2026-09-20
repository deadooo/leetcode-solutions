                
def twoSum(nums, target):
    for index1, num1 in enumerate(nums):
        for index2, num2 in enumerate(nums):
            if(num1 + num2 == target and index1 != index2):
                return (index1, index2)
# Testing
nums = [2,7,11,15]
target = 9
print(f"Input: {nums}")
print(f"Output: {twoSum(nums, target)}")

# Notes
# Runned 3000ms try to lower to < 30ms
# Running in n(o2) try to beat it
# Don't forget to account for negatives