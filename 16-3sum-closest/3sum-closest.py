class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = nums[0] + nums[1] + nums[-1]
        

        for cursor in range(len(nums)):
            
            left = cursor + 1
            right = len(nums)-1
            
            while left < right:
                
                newValue = nums[cursor] + nums[left] + nums[right]
                closest =  newValue if abs(closest - target) > abs(newValue - target) else closest

                if newValue < target:
                    left += 1
                else:
                    right -= 1

        return closest