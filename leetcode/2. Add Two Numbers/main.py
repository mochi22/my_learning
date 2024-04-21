#https://leetcode.com/problems/add-two-numbers/submissions/1238044660/?envType=list&envId=xo2bgr0r

"""
ListNodeなるものを使用する。方向のあるリストだと考えればよい。
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""


# kuraryu's answer (最悪計算量O(2N+1)、平均計算量O(N)、Nは与えられたリストのうちの長い方のリストの長さ)
# おそらく平均計算量はこれ以上早くできないし、最悪計算量もそこまで悪くないのでまあまあなできな気がした
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        above_value = 0
        sum_value = []

        while True:
            if l1 == None:
                l1_value = 0
            else:
                l1_value = l1.val
            if l2 == None:
                l2_value = 0
            else:
                l2_value = l2.val

            value = l1_value + l2_value

            if above_value == 1:
                value += 1
                above_value = 0

            # max value == 18, because 0<=node.val<=9
            # if above_value == 1 --> max value == 19
            if value >= 10:
                above_value = 1
                value -= 10

            sum_value.append(value)

            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next

            if l1 == None and l2 == None:
                if above_value == 1:
                    sum_value.append(1)
                    break
                else:
                    break
        print(sum_value)
        prev_val = None
        for i in reversed(sum_value):
            print(i)

            if prev_val is None:
                print("this is none")
                val = ListNode(i, None)
                
            else:
                val = ListNode(i, prev_val)
            prev_val = val
            print("val",val.val, val.next)
        print(val)
        return val




## 模範解答
# 最悪計算量および平均計算量がO(N)だし、スマート。こんな感じにかけるとよかった。なんも見ずにこの程度はかけないといけない。


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        tail = dummyHead
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            digit1 = l1.val if l1 is not None else 0
            digit2 = l2.val if l2 is not None else 0

            sum = digit1 + digit2 + carry
            digit = sum % 10
            carry = sum // 10

            newNode = ListNode(digit)
            tail.next = newNode
            tail = tail.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        result = dummyHead.next
        dummyHead.next = None
        return result