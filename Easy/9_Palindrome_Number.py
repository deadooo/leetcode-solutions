# class Solution(object):
#     def isPalindrome(self, x):
#         """
#         :type x: int
#         :rtype: bool
#         """

def isPalindrome(x):
    i = 0
    count = 0
    PNum = 0
    if(x < 0):
        return False
    temp = x
    while temp >= 10: # Iteration Range
        temp = temp // 10
        i += 1
    temp = x
    while temp >= 1:
        M_Divide = (10 ** i) # First Digit Getter
        TempFirstDigit = int(temp / M_Divide)
        print(f"FD:{TempFirstDigit}")
        
        Subtract = (10 ** i) * TempFirstDigit # First Digit Remover
        temp = temp - Subtract
        print(f"CN:{temp}")
        i -= 1
        
        PNum += TempFirstDigit * (10 ** count)
        count+=1
    if x == PNum:
        return True
    return False    
    

# Testing
x = 123454321
print(f"Input: x = {x}")
print(f"Output: {str(isPalindrome(x))}")

x = -121
print(f"Input: x = {x}")
print(f"Output: {str(isPalindrome(x))}")


# Notes
# Was able to do the extra requirement of not using String Conversion!