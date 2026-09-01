class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        f, l = 0, len(matrix) - 1
        while f <= l:
            hoz = f + (l - f) // 2
            if matrix[hoz][0] == target:
                return True
            elif (hoz == len(matrix) - 1 and target > matrix[hoz][0]) or (hoz + 1 < len(matrix) and matrix[hoz + 1][0] > target > matrix[hoz][0]):
                lf, r = 0, len(matrix[hoz]) - 1
                while lf <= r:
                    mid = lf + (r - lf) // 2
                    if matrix[hoz][mid] == target:
                        return True
                    elif matrix[hoz][mid] > target:
                        r = mid - 1
                    else:
                        lf = mid + 1 
                return False
            elif matrix[hoz][0] > target:
                l = hoz - 1
            else:
                f = hoz + 1 
        
        return False