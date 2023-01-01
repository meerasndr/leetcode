from typing import List
def getConcatenation(nums: List[int]) -> List[int]:
    ans = []
    n = len(nums)
    times = 0
    while(times < 2):
        for i in range(0, n):
            ans.append(nums[i])
        times += 1
    return ans

print(getConcatenation([1,2,1]))