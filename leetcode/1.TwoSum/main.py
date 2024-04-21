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
    


## Solution2 (Two-pass Hash Table)
"""
まず、hash tableを作成する。(ここでO(n))
hash table に対して必要なcomplementを算出して条件に合致すると終了する。(ここでO(n))
"""
# 最悪計算量O(2n) ==> 計算量O(n)
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> numMap;
        int n = nums.size();

        // Build the hash table
        for (int i = 0; i < n; i++) {
            numMap[nums[i]] = i;
        }

        // Find the complement
        for (int i = 0; i < n; i++) {
            int complement = target - nums[i];
            if (numMap.count(complement) && numMap[complement] != i) {
                return {i, numMap[complement]};
            }
        }

        return {}; // No solution found
    }
};
    

## Ideal code (One-pass Hash Table)
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
