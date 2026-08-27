class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        nums.sort()
        for i in range(n - 2):
            if i == 0 or nums[i] != nums[i - 1]:
                target = -nums[i]
                resultant_list = self.twoSum(nums[i + 1:], target)
                for res in resultant_list:
                    if res:
                        result.append([nums[i], res[0], res[1]])
        return result



    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        n = len(nums)
        if n > 2:  
            nums.sort()
        left, right = 0, n - 1
        res = []
        while left < right:
            if nums[left] + nums[right] == target:
                res.append([nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1  
                left += 1
                right -= 1                 
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1
        return res      