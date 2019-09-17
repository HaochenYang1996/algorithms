# attempt 1
# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         res = {}
#         lst = {}

#         # "index" is a number in nums, "value" is its index in nums
#         # if the list is [2,7,11,15]
#         # lst's indicies 2 7 11 15 correspond to 0 1 2 3 
#         for i in range(len(nums)):
#         	lst[nums[i]] = i

#         for i in range (len(nums)):
#         	t = target - nums[i]
#         	if (nums.count(t)!=0 and lst[t]!=i):
#             	    res = [lst[t],i]	
#         return res


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # if the nums is [2,7,11,15]
        # lst's indicies 2 7 11 15 correspond to 0 1 2 3 
        lst={}
        res={}
        # enumerate(nums) gives (inedex, value)
        for i, num in enumerate(nums):
            t = target - num
            if t not in lst:
                lst[num] = i
            else
                res = [lst[t],i]
        return res
