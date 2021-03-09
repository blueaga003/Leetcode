# Leetcode: 448. Find All Numbers in Disappeared Array

class Solution:
    def findDisappearedNumbers(self, nums):
        length_of_nums = len(nums)
        output_list = []
        i = 1
        
        # Base case
        if length_of_nums < 1:
            return output_list
        
        # Changing to set for O(1) lookup time
        nums = set(nums)
        
        while i <= length_of_nums:
            if i not in nums:
                output_list.append(i)
            i += 1
            
        return output_list

if __name__ == "__main__":
    solution = Solution()
    print(solution.findDisappearedNumbers([2, 3]))
