class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        nums.sort()

        result = []

        for i in range(len(nums)-2): # sıralama nums listesinin sonunda [i,j,k] olacak.
            
            # aynı sayıları tekrar denememek için atlama
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            j = i+1
            k = len(nums)-1

            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum > 0:
                    k -= 1
                    continue
                elif sum < 0:
                    j += 1
                    continue
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    k -= 1
                    j += 1

                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
        return result