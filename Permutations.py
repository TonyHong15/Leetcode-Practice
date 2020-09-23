from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0 or len(nums) == 1:
            return [nums]
        else:
            permlist = []
            for i in range(len(nums)):
                permutations = self.permute(nums[:i] + nums[i+1:])
                for p in permutations:
                    permlist.append([nums[i]] + p)
            return permlist


if __name__ == '__main__':
    pass

