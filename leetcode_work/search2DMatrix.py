"""
Leetcode Medium

Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

Exaple 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
"""

# My attempt: binary search within binary search
def searchSubMatrix(matrix, target, i):
    # check if in array
    if not (matrix[i][0] <= target and target <= matrix[i][len(matrix[i])-1]):
        return False

    # search for target
    mid = 0
    low = 0
    high = len(matrix[i])-1

    while (low <= high):
        mid = (low + high /2)
        if (matrix[i][mid] > target):
            high = mid -1 
        elif (matrix[i][mid < target]):
            low = mid + 1
        else:
            return True
            
class Solution(object):
    
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # implement binary search 
        mid = 0
        low = 0
        high = len(matrix)-1
        
        while(low <= high):
            mid = (low + high)/2
            found = searchSubMatrix(matrix, target, mid)
            if found:
                return True
            if (matrix[mid][0] > target):
                high = mid -1
            elif(matrix[mid][len(matrix[mid])-1]):
                low = mid + 1
        return False
                
# Notes: len() is O(1)
# Try not to get too caught up in forcing an algorithm to fix the problem
# C++ size() is O(1) too

"""
A C++ solution I really liked
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int rows = matrix.size(), 
            cols = matrix[0].size(),
            row = 0, 
            col = cols - 1;
			
        while (row < rows && col > -1) {
            int cur = matrix[row][col];
            if (cur == target) return true;
            if (target > cur) row++;
            else col--;
        }
        
        return false;
    }
};
"""
        


