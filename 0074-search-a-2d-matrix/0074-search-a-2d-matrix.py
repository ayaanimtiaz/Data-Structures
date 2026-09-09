class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        conf = False

        right = len(matrix) -1 
        right_s = len(matrix[0]) - 1
        left = 0
        left_s = 0
        middle = (right + left) // 2
        middle_s = (right_s + left_s) // 2
        # maybe we start at the first element for each row
        # continue to wind down until we reach one row
        # do binary search that way

        while left <= right:
            if matrix[middle][0] == target:
                return True
            elif matrix[middle][0] > target:
                right = middle - 1
                middle = (right + left) // 2
            elif matrix[middle][0] < target:
                left = middle + 1
                middle = (right+left) // 2
    
        while left_s <= right_s:
            if matrix[middle][middle_s] == target:
                return True
            elif matrix[middle][middle_s] > target:
                right_s = middle_s - 1
                middle_s = (right_s + left_s) // 2
            elif matrix[middle][middle_s] < target:
                left_s = middle_s + 1
                middle_s = (right_s + left_s) // 2

        return False