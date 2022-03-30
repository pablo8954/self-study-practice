"""
9 - Palindrome Number (Easy)
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.
 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        """
        first rightmost digit
        121 / 10 = 12 
        121 % 10 = 1
        
        second rightmost digit
        12 / 10 = 1 
        12 % 10 = 2
        
        nth rightmost digit
        1 / 10 = 0
        1 % 10 = 1
        
        first rightmost digit 
        121 / 10 = 12
        121 % 10 = 1
        
        nth digit 
        121 / 10^2 = 121 / 100 = 1
        dontcare about module
        """
        
        # handle if negative value
        if x < 0:
            return False
        
        # decode up to which power of 10 (In the 10s, 100s, 1000s?)
        if x > 0:
            digits = int(math.log10(x))+1
        else: 
            return True
        
        # using power of 10, loop thru front and back until reaching middle
        i = 1
        j = digits - 1
        
        while (i <= j):
            rightDigit = x % (10**i)
            leftDigit = x / (10**j)

            if not (rightDigit == leftDigit):
                return False
            i = i + 1
            j = j - 1
        
        return True

