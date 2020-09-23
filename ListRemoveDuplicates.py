from typing import List


def removeDuplicates(nums: List[int]) -> int:
    if len(nums) == 0 or len(nums) == 1:
        return len(nums)
    else:
        temp = nums[0]
        count = 1
        for x in range(1, len(nums)):
            if temp == nums[count]:
                nums.pop(count)
            else:
                temp = nums[count]
                count += 1
        return len(nums)


class Solution:
    pass


if __name__ == '__main__':
    list1 = [1,2, 2,3,3]
    print(removeDuplicates(list1))
    print(list1)

