
# 以下の各ステップを実装すればよい。
        # step1: ignore blank
        # step2: read "-" or "+"
        # step3: read next characters until the next is non-disit or end
        # step4: convert str to int
        # step5: range -2^31 <= return <= 2^31-1

# 1st 20分くらいかかったけどどうにか実装できた。
# time complexity O(N)
# space complexity 最悪の場合を考えるとresultが長さNになるのでO(N)かな?(自信ない)
class Solution:
    def myAtoi(self, s: str) -> int:
        # step1: ignore blank
        # step2: read "-" or "+"
        # step3: read next characters until the next is non-disit or end
        # step4: convert str to int
        # step5: range -2^31 <= return <= 2^31-1

        if s == "" or s == "+" or s == "-":
            return 0

        result = ""
        sign = 1

        # step1: ignore blank
        for i in range(len(s)):
            if s[i] == " ":
                pass
            else:
                # step2: read "-" or "+"
                if s[i] == "-":
                    sign = -1
                    i+=1
                elif s[i] == "+":
                    # sign = 1 # いらない
                    i+=1
                break
            
        print(s[i:], s[i], i)
            
        # step3: read next characters until the next is non-disit or end
        for i in range(i, len(s)):
            try:
                intger_i = int(s[i])
                result += s[i]

            except:
                print("aa", i, s[i])
                break
        print(result)
        # step4: convert str to int
        if result == "":
            result = 0
        else:
            result = int(result) * sign
        print(result)

        # step5: range -2^31 <= return <= 2^31-1
        if -2**31 > result:
            result = -2**31 
        elif result >= 2**31  - 1:
            result = 2**31  - 1
        return result
        

# 参考コード c++ をchatgptでpythonに変形
# https://leetcode.com/problems/string-to-integer-atoi/solutions/3202876/best-c-solution-ever-easy-to-understand-string-one-stop-solution/?envType=list&envId=xo2bgr0r
"""
class Solution:
    def myAtoi(self, s: str) -> int:
        # 計算量: O(n) (nは文字列sの長さ)
        # 空間計算量: O(1)
        
        len_s = len(s)
        num = 0
        i = 0
        
        # 先頭の空白文字をスキップ
        while i < len_s and s[i] == ' ':
            i += 1
        
        # 正負の符号をチェック
        # ここのtry exceptだけ追加した。
        try:
            positive = s[i] == '+'
            negative = s[i] == '-'
        except:
            # ここに来るのはs[i]がないとき
            return 0

        if positive or negative:
            i += 1
        
        # 数値の抽出
        while i < len_s and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1
        
        # 符号を反映
        if negative:
            num = -num
        
        # INT_MAXとINT_MINの範囲内に収める
        num = min(max(num, -2**31), 2**31 - 1)
        
        return num
"""

#以下の方がぱっと見で良さそう
#https://github.com/cheeseNA/leetcode/pull/5/files#diff-f22741bbaf0a18e8ce4187aeb6e1c20b03359fd629214176777b0cd40fb3b632
"""
class Solution:
    def myAtoi(self, s: str) -> int:
        UPPER_BOUND = 2 ** 31 - 1
        LOWER_BOUND = -(2 ** 31)
        index = 0
        is_positive = True
        abs_value = 0
        while index < len(s) and s[index] == " ":
            index += 1
        if index < len(s) and s[index] in "+-":
            if s[index] == "-":
                is_positive = False
            index += 1
        while index < len(s) and s[index].isdigit():
            abs_value *= 10
            abs_value += int(s[index])
            if is_positive and abs_value >= UPPER_BOUND:
                return UPPER_BOUND
            if not is_positive and -1 * abs_value <= LOWER_BOUND:
                return LOWER_BOUND
            index += 1
        return abs_value * (1 if is_positive else -1)
"""


# 2nd
class Solution:
    def myAtoi(self, s: str) -> int:
        UPPER_LIMIT = 2**31 - 1
        UNDER_LIMIT = -2**31

        index = 0
        is_Positive = True
        result = 0

        while index < len(s) and s[index] == " ":
            index += 1

        if index < len(s) and s[index] in "+-":
            if s[index] == "-":
                is_Positive = False
            index += 1
        while index < len(s) and s[index].isdigit():
            result *= 10
            result += int(s[index])
            index += 1
        
        # 以下の感じでできそうだと思ったけど、かなり複雑になるので分けた方がよい。
        # while index < len(s):
        #     if s[index] == " ":
        #         index += 1

        #     elif index < len(s) and s[index] in "+-":
        #         if s[index] == "-":
        #             is_Positive = False
        #         index += 1

        #     elif index < len(s) and s[index].isdigit():
        #         result *= 10
        #         result += int(s[index])
        #         index += 1
        #     else:
        #         # if result != 0:
        #             # break
        #         # index += 1
        #         break
        

        result = result if is_Positive else -1*result

        if result >= UPPER_LIMIT:
            return UPPER_LIMIT
        if result <= UNDER_LIMIT:
            return UNDER_LIMIT
        return result
"""
https://docs.python.org/ja/3/library/stdtypes.html
str.isdigit()
文字列中の全ての文字が数字で、かつ 1 文字以上あるなら True を、そうでなければ False を返します。ここでの数字とは、十進数字に加えて、互換上付き数字のような特殊操作を必要とする数字を含みます。また 10 を基数とした表現ができないカローシュティー数字のような体系の文字も含みます。正式には、数字とは、プロパティ値 Numeric_Type=Digit または Numeric_Type=Decimal を持つ文字です。
"""


# 3rd-1
class Solution:
    def myAtoi(self, s: str) -> int:
        UPPER_LIMIT = 2**31 - 1
        UNDER_LIMIT = -2**31

        result = 0
        is_positive = True
        index = 0

        while index < len(s) and s[index] == " ":
            index += 1
        
        if index < len(s) and s[index] in "+-":
            if s[index] == "-":
                is_positive = False
            index += 1
        

        
        # s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'
        # so isdigit can use
        while index < len(s) and s[index].isdigit():
            result = result * 10 + int(s[index])
            index += 1
        
        if not is_positive:
            result *= -1

        if result > UPPER_LIMIT:
            return UPPER_LIMIT
        elif result < UNDER_LIMIT:
            return UNDER_LIMIT

        return result

# 3rd -2
class Solution:
    def myAtoi(self, s: str) -> int:

        #https://hantaigo.com/word/upper#google_vignette
        # upper（上のほうの）	⇔	lower（下のほうの）

        UPPER_LIMIT = 2**31 - 1
        LOWER_LIMIT = -2**31 

        index = 0
        result = 0
        is_positive = True

        while index < len(s) and s[index] == " ":
            index += 1
        
        if index < len(s) and s[index] in "+-":
            if s[index] == "-":
                is_positive = False
            index += 1
        
        # この書き方は微妙かな。
        # if index < len(s) and s[index] == "+":
        #     index += 1

        # s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'. => .isdigit() can use
        while index < len(s) and s[index].isdigit():
            result = result * 10 + int(s[index])
            index += 1
        
        if not is_positive:
            result *= -1
        
        if UPPER_LIMIT < result:
            return UPPER_LIMIT
        if result < LOWER_LIMIT:
            return LOWER_LIMIT 
        return result

# 3rd -3
class Solution:
    def myAtoi(self, s: str) -> int:
        UPPER_LIMIT = 2**31 - 1
        LOWER_LIMIT = -2**31

        index = 0
        result = 0
        is_positive = True

        while index < len(s) and s[index] == " ":
            index += 1
        
        if index < len(s) and s[index] in "+-":
            if s[index] == "-":
                is_positive = False
            index += 1
        
        # s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.  => .isdigit() can use
        while index < len(s) and s[index].isdigit():
            result = result * 10 + int(s[index])
            index += 1
        
        if not is_positive:
            result *= -1
        
        if result < LOWER_LIMIT:
            return LOWER_LIMIT
        if UPPER_LIMIT < result:
            return UPPER_LIMIT
        return result