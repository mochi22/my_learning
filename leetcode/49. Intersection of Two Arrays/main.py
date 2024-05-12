macの方で解いた気がするのでいったん置いとく
## 1st
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # num1 と num2 のリスト間で共通のものを求める。 -> set 使えば一瞬.
        # set 以外での解法としては、片方を for ですべて確認して、ユニークなキーをもつdictを作成して、もう一方がそのキーを持つか判定して、キーを削除していって、最終的にキーがすべてなくなれば ok
        # ざっくりと残二つしか思いつかなかった。->簡単に作成できるsetを使用した方法から書いていく。


        set_nums1 = set(nums1)
        set_nums2 = set(nums2)

        return set_nums1 & set_nums2

