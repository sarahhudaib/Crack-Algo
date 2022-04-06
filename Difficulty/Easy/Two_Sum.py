class Solution:
    def twoSum(self, nums: list[int], target: int):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        """ iterate through the list and store the index of each 
        element in the hashmap with the value as the element itself  """
        for i, v in enumerate(nums):
            # check if the difference between the target and the current element is in the hashmap
            if v in hashmap:
                return [hashmap[v], i]
            # subtract the current element from the target and store it in the hashmap
            # then store the index of the current element in the hashmap
            hashmap[target - v] = i


if __name__ == '__main__':
    s = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    print(s.twoSum(nums, target))

    print(s.twoSum([3, 7, 3, 6], 9))
