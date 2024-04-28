# https://leetcode.com/problems/two-sum/description/?envType=list&envId=xo2bgr0r

"""
感想

正直brute forceの回答しか思いつかなかった。
まあ、hash tableの使い方が勉強になったので類似問題はこれで解く。
"""


## Brute Force
"""
全探索していって条件に合致したら終了
"""
# 最悪計算量O(n^2)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []  # No solution found
    


## 2nd (Hash Table)
"""
hash table作成を行わないsolution
数値の組み合わせは必ず二回扱われる(呼び出されるのに近い)ので、一回目はhash tableに保存し二回目でhash tableから算出して終了する。
"""
# 最悪計算量O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap={}
        length = len(nums)

        for i in range(length):
            complement = target - nums[i]

            if complement in numMap:
                return [i, numMap[complement]]
            else:
                numMap[nums[i]] = i
        return []
