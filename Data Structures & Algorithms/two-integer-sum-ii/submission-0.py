class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 


        n = len(nums)
        if n > 2:  
            nums.sort()
        left, right = 0, n - 1
        while left < right:
            if nums[left] + nums[right] == target:
                return [left + 1, right + 1]
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1
        return [-1, -1]        
        