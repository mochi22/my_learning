
# 1st
# なんとなく方針は立ったが解けなかった
# 以下の解法が参考になる。単純にインデックスを見るとdownなら+1だし、not downなら-1なので、インデックスの足し算、引き算で簡単に実装できた
#https://leetcode.com/problems/zigzag-conversion/solutions/5004842/video-simple-solution/?envType=list&envId=xo2bgr0r
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if len(s) == 1:
            return s
            
        down = 1
        result = [""]*numRows

        # 謎の特性(細かい決まりとかによると思われるがさくっと調べてもでてこなかったのでいったん放置)
        # result = [[]]*numRows
        # result[0].append(1)
        # print(result) # [[1], [1], [1]]
        # a = [[],[],[]]
        # a[0].append(1)
        # print(a) # [[1], [], []]

        # listで考える。numRowsだけ下がり、同じ数だけ上がる。移動するたびにlist内の文字列に連結する。最後に結合する。
        # ["P","",""] -> ["P","A",""] -> ["P","A","Y"] -> ["P","AP","Y"] -> ["PA","AP","Y"] ...

        # i%numRows-1でいい感じにできそう
        
        for i in range(len(s)):
            list_index = i % numRows
            if down==1:
                result[list_index] += s[i]
            else:
                print("down!=1", list_index, list_index-2*(list_index+1))
                #index0 -> index-2, index1->index-3
                #index0 -> index-2, index1 -> index-3, index2 -> index-4
                result[list_index-2*(list_index+1)] += s[i]
                if list_index == numRows-2:
                    down *= -1
            if list_index == (numRows-1):
                down *= -1

            print(list_index, result, s[i])
        
        return result


# 2nd
# いい感じにできたように思えるが、directは冗長なのでもっと楽にかけそう。
# 参考コードより、文字列リストではなく、二重リストの方がいいのかがわからない。好みの問題なら文字列の方がわかりやすいと感じるのでこちらを使う。
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) == 1 or numRows==1:
            return s
        result_index = 0
        direct = "down"
        tmp_list = [""] * numRows

        for i in range(len(s)):
            
            tmp_list[result_index] += s[i]
            
            if result_index % numRows == numRows-1:
                direct = "up"
            elif result_index % numRows == 0:
                direct = "down" 
            
            if direct == "down":
                result_index += 1
            else:
                result_index -= 1
        
        
        result = "".join(tmp_list)
        print(result)
        return result


# ただ、参考にした下記コードでは二重リストと文字列で違いとして、計算量が違うといってるがどちらも時間計算量O(n)になるのではないかと考えた

#https://leetcode.com/problems/zigzag-conversion/solutions/5004842/video-simple-solution/?envType=list&envId=xo2bgr0r
"""
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        idx, d = 0, 1
        rows = [[] for _ in range(numRows)]

        for char in s:
            rows[idx].append(char)
            if idx == 0:
                d = 1
            elif idx == numRows - 1:
                d = -1
            idx += d

        for i in range(numRows):
            rows[i] = ''.join(rows[i])

        return ''.join(rows)  

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        idx, d = 0, 1
        rows = [''] * numRows

        for char in s:
            rows[idx] += char
            if idx == 0:
                d = 1
            elif idx == numRows - 1:
                d = -1
            idx += d

        return ''.join(rows)  
"""


## 3-1
# len(s)==1よりも、numRows >= len(s)の方が汎用的。
class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if len(s) == 1 or numRows==1:
            return s
        index = 0
        direct = 1
        str_rows = [""] * numRows

        for i in range(len(s)):
            str_rows[index] += s[i]

            if index % numRows == 0:
                direct = 1
            elif index % numRows == numRows-1:
                direct = -1

            index += direct
        
        result = "".join(str_rows)
        return result

## 3-2
class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1 or len(s) < numRows:
            return s
        
        index = 0
        direct = 1
        str_rows = [""]*numRows

        for i in range(len(s)):
            str_rows[index] += s[i]

            if index % numRows == numRows - 1:
                direct = -1
            elif index == 0:
                direct = 1
            index += direct
            
            
        result = "".join(str_rows)
        return result 

#3-3(3-2と同じになっちゃったので、別の解法を試した。)
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows==1 or len(s) < numRows:
            return s

        list_rows = [[] for _ in range(numRows)]
        print(list_rows)
        direct = 1
        index = 0
        for i in range(len(s)):
            list_rows[index].append(s[i])

            if index == 0:
                direct = 1
            elif index % numRows == numRows - 1:
                direct = -1

            index += direct
        print(list_rows)
        for i in range(len(list_rows)):
            list_rows[i] = "".join(list_rows[i])
        print(list_rows)
        return "".join(list_rows)