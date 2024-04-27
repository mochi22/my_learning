# https://leetcode.com/problems/longest-substring-without-repeating-characters/?source=submission-noac

"""
文字列中のなかでユニークな単語の長さを求める。
正直ぱっとみではbrute forceの解放しか思いつかなかったし、brute forceの解放も汚くなってる
"""


## kuraryu's solution
# brute forceでほぼ全探索した。(最悪計算量はO(n^2)、平均計算量はO(n^2)かな)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        length = len(s)
        max_count = 1 if length!=0 else 0
        count = 1
        pasted = []




        for i in range(length):
            start_str = s[i]
            pasted.append(start_str)
            for j in range(length):
                if j > i:
                    
                    end_str = s[j]
                    

                    if end_str in pasted:
                        if max_count < count:
                            max_count = count
                        count = 1
                        pasted = []

                        break
                    else:
                        pasted.append(end_str)
                        count+=1
                        if max_count < count:
                            max_count = count
                    # print(start_str, end_str, count, pasted, max_count)
        print(max_count)
        return max_count



### 解法

## Setを使う方法
# 計算量はO(n)だし、めちゃめちゃシンプルな解法

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxLength = 0
        charSet = set()
        left = 0
        
        for right in range(n):
            if s[right] not in charSet:
                charSet.add(s[right])
                maxLength = max(maxLength, right - left + 1)
            else:
                while s[right] in charSet:
                    charSet.remove(s[left])
                    left += 1
                charSet.add(s[right])
        
        return maxLength


## setの代わりにunoerderd map(dictなだけ？)を使う方法
# setの奴とほぼ同じ
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxLength = 0
        charMap = {}
        left = 0
        
        for right in range(n):
            if s[right] not in charMap or charMap[s[right]] < left:
                charMap[s[right]] = right
                maxLength = max(maxLength, right - left + 1)
            else:
                left = charMap[s[right]] + 1
                charMap[s[right]] = right
        
        return maxLength


## interger array()
# [-1] * 128であるのは文字のユニークな個数かな。s.length<=5*10^4なので128じゃ不足しそうなのにしない。
# ord(a)==97
# 完全な理解には及んでないかも

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxLength = 0
        charIndex = [-1] * 128
        left = 0
        
        for right in range(n):
            if charIndex[ord(s[right])] >= left:
                left = charIndex[ord(s[right])] + 1
            charIndex[ord(s[right])] = right
            maxLength = max(maxLength, right - left + 1)
        
        return maxLength
    



### 2nd (解法見たうえでの回答)
"""
whileの使い方にとまどった。
以下はメモ(これくらいは知っとくべきなので暗記しとく)

print(1==1 or 2==1) #True
print(1==1 or 2!=1) #True
print(1!=1 or 2==1) #False
print(1!=1 or 2!=1) #True

print(True or False)  #True
print(True or True)   #True
print(False or False) #False
print(False or True)  #True

print(True and False)  #False
print(True and True)   #True
print(False and False) #False
print(False and True)  #False
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sets = {}
        result=0
        left=0

        for right in range(len(s)):
            if s[right] not in sets:
                sets.add(s[right])
                result = max(result, right-left+1)
            else:
                while s[right] in sets:
                    print(left, right, sets, s[right], s[left])
                    sets.remove(s[left])
                    left +=1
                sets.add(s[right])
            print("aaa")
        return result
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maps = {} #maps[char]=index
        left = 0
        result=0


        for right in range(len(s)):
            # print(left, right, maps, result)
            # ignore less than left indexes
            if s[right] not in maps or maps[s[right]] < left:
                # maps[s[right]] = right
                result = max(result, right-left+1)
            else:
                #left index += 1
                left= maps[s[right]] + 1 
            maps[s[right]] = right
        return result


