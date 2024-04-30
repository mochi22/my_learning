## 1st
# ({})とかもTrueになる場合の実装がパッと思いつかず5分経過した

class Solution:
    def isValid(self, s: str) -> bool:
        #s consists of parentheses only '()[]{}'

        
        index = 0
        result = False

        while index < len(s):
            print(index, s[index])
            if len(s[index:]) == 1:
                return result
            elif s[index] in ")]}":
                print("111")
                # result = False
                index += 1
            elif (s[index] == "(" and s[index+1] == ")") or (s[index] == "[" and s[index+1] == "]") or (s[index] == "{" and s[index+1] == "}") :
                print("222")
                result = True
                index = index+2
            else:
                print("333")
                # result = False
                index += 1
        return result


# 2nd
# leetcode上の解放を真似た。ただ、リテラル(")}]"とか)を使ってるのはよくないはずなので、他の方の解放をまねる。
class Solution(object):
    def isValid(self, s):
        stack = []

        for index in range(len(s)):
            if s[index] in "({[":
                stack.append(s[index])
            
            if s[index] in ")}]":
                if (not stack) or (stack[-1] != "(" and s[index] == ")") or (stack[-1] != "{" and s[index] == "}") or (stack[-1] != "[" and s[index] == "]"):
                    return False
                else:
                    stack.pop()

        if len(stack) >= 1:
            return False
        return True

https://github.com/sakupan102/arai60-practice/pull/7/files
```
class Solution:
    def isValid(self, s: str) -> bool:
        open_to_close = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        brackets_stack = []
        for char in s:
            if char in open_to_close:
                brackets_stack.append(char)
                continue
            if not brackets_stack:
                return False
            open_brackets = brackets_stack.pop()
            if open_to_close[open_brackets] != char:
                return False
        return not brackets_stack
```

2nd - 2

class Solution(object):
    def isValid(self, s):
        open_to_close = {
            "(" : ")",
            "{" : "}",
            "[" : ']'
        }
        
        # 英語は以下の対応らしい->parenthesesというよりかはbracketsの方が含む記号の数が多いので適してるかな。
        #parentheses==()
        #square brackets==[]
        #curly brackets=={}
        #angle brackets==<>
        # あくまでもstackなのでstackの方が先にもってきた。bracketsでもいいが、openしか入らないのでopensとしたが、そこまで頭が回らないので単にstack_bracketsでいい気がする。
        stack_opens = []
        
        # charがopenではない == closeである
        # reason -> s consists of parentheses only '()[]{}'
        for char in s:
            if char in open_to_close:
                stack_opens.append(char)
                continue
            
            if len(stack_opens) == 0:
                return False
            
            if char != open_to_close[stack_opens.pop()]:
                return False
            print(char)

        return not stack_opens

# close_to_openだと以下のコードになる。「if stack_opens.pop() != close_to_open[char]:」あたりはこっちの方が好きだが、好みだしopen_to_closeの方が最初は定義しやすいかな。
```
class Solution(object):
    def isValid(self, s):
        close_to_open = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        
        stack_opens = []
        
        for char in s:
            if char not in close_to_open:
                stack_opens.append(char)
                continue
            
            if len(stack_opens) == 0:
                return False
            
            if stack_opens.pop() != close_to_open[char]:
                return False

        return not stack_opens
````
## 3rd - 1
class Solution(object):
    def isValid(self, s):
        stack_brackets = []

        open_to_closes = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        } 

        for char in s:
            if char in open_to_closes:
                stack_brackets.append(char)
                continue
            
            if not stack_brackets:
                return False
            
            select_open = stack_brackets.pop()

            if char != open_to_closes[select_open]:
                return False

        
        return not stack_brackets

## 3rd - 2
class Solution(object):
    def isValid(self, s):

        open_to_closes = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }

        stack_brackets = []

        for char in s:
            if char in open_to_closes:
                stack_brackets.append(char)
                continue
            #まとめたい気もするが、pop()しときたいのでこのままが良さそう。
            if not stack_brackets:
                return False
            select_open = stack_brackets.pop()
            if char != open_to_closes[select_open]:
                return False
        return not stack_brackets



## 3rd - 3
class Solution(object):
    def isValid(self, s):
        open_to_closes = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }

        stack_brackets = []

        for char in s:
            if char in open_to_closes:
                stack_brackets.append(char)
                continue
            if not stack_brackets:
                return False
            select_open = stack_brackets.pop()
            if char != open_to_closes[select_open]:
                return False
        return not stack_brackets
