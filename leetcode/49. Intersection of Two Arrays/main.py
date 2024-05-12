macの方で解いた気がするのでいったん置いとく
## 1st
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # num1 と num2 のリスト間で共通のものを求める。 -> set 使えば一瞬.
        # 数とか順番とかは気にしなくて良いので、setを使えって & の数値のみreturnすれば良さそう。
        # set 以外での解法としては、片方を for ですべて確認して、ユニークなキーをもつdictを作成して、もう一方がそのキーを持つか判定して、キーを削除していって、最終的にキーがすべてなくなれば ok
        # ざっくりと残二つしか思いつかなかった。->簡単に作成できるsetを使用した方法から書いていく。

        set_nums1 = set(nums1)
        set_nums2 = set(nums2)

        return list(set_nums1 & set_nums2)

# => 瞬殺

## 2nd

# set使わない方法だと、
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # set 使わない方法を考える。
        # list で hashmap を使う方法が考えられる。
        # 具体的には、nums1のそれぞれの数値をキーとして追加していき、

        num1_dict = {}
        result = []
        for num1 in nums1:
            num1_dict[num1] = 1
        for num2 in nums2:
            if num2 in num1_dict and num2 not in result:
                result.append(num2)
        return result


# dictである必要がないので list にした。
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        num1_list = []
        result = []
        for num1 in nums1:
            num1_list.append(num1)
        for num2 in nums2:
            if num2 in num1_list and num2 not in result:
                result.append(num2)
        return result
        
        

## 3rd 
# 参考: https://github.com/hayashi-ay/leetcode/pull/21/files

# listがreturnされるように list にする
# intersection == &

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))
