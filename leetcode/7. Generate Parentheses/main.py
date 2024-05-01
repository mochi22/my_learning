### 1st

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        processing_parentheses = "("
        
        open_parentheses_count = 1
        close_parentheses_count = 0

        ### 考え方
        # formed というのは、単純に左から数えた時に「"(”の数 >= ")"の数」となるようになる組み合わせを全探索する。(n=8だし..)

        # 最初は")"の数 = 0なので、必ず "("
        # "(" -> どちらでもよい。 
        # "((" -> どちらでもよい or "()" -> 必ず"("
        # "(((" -> どちらでもよい or "(()" -> どちらでもよい or "()(" -> "どちらでもよい"
        # ...
        # どちらでも良いという操作はnの数次第

        def addParentheses(open_parentheses_count, close_parentheses_count, processing_parentheses):
            # 最初は必ずopen
            # 一つあたり max 2n
            if len(processing_parentheses) == n * 2:
                # 数が一致したらok
                if open_parentheses_count == close_parentheses_count:
                    result.append(processing_parentheses)
                return 
            
            # parenthesesの数のうち片方がn以上になると必ずダメな組みわせ
            if open_parentheses_count > n or close_parentheses_count > n:
                return
            
            # 必ず"("
            if open_parentheses_count == close_parentheses_count:
                addParentheses(open_parentheses_count + 1, close_parentheses_count, processing_parentheses + '(')

            # どちらでもよい.
            if open_parentheses_count > close_parentheses_count:
                addParentheses(open_parentheses_count + 1, close_parentheses_count, processing_parentheses + '(')
                addParentheses(open_parentheses_count, close_parentheses_count + 1, processing_parentheses + ')')

        # 再帰関数を実行
        addParentheses(open_parentheses_count, close_parentheses_count, processing_parentheses)
        return result


### 2nd
#変数名とifのまとまりの変更くらい。元々かなりまとまってるように思える。
#open, close -> left, rightでもどっちでも良い。
# 時間がなくてためせてないが、defを定義せずに実装してる方法もあるのでこの方法でも実装しておきたい。(4thとかの課題)
#https://github.com/SuperHotDogCat/coding-interview/pull/7/files
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        processing_parentheses = "("
        
        open_parentheses_num = 1
        close_parentheses_num = 0
        
        def addParentheses(open_parentheses_num, close_parentheses_num, processing_parentheses):

            if len(processing_parentheses) == n * 2:
                if open_parentheses_num == close_parentheses_num:
                    result.append(processing_parentheses)
                return 
            elif open_parentheses_num > n or close_parentheses_num > n:
                return

            if open_parentheses_num == close_parentheses_num:
                addParentheses(open_parentheses_num + 1, close_parentheses_num, processing_parentheses + '(')
            elif open_parentheses_num > close_parentheses_num:
                addParentheses(open_parentheses_num + 1, close_parentheses_num, processing_parentheses + '(')
                addParentheses(open_parentheses_num, close_parentheses_num + 1, processing_parentheses + ')')

        # 再帰関数を実行
        addParentheses(open_parentheses_num, close_parentheses_num, processing_parentheses)
        return result


### 3rd - 1

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        procese_parentheses = "("
        open_parentheses_num = 1
        close_parentheses_num = 0

        def addParentheses(open_parentheses_num, close_parentheses_num, procese_parentheses):

            if len(procese_parentheses) == 2 * n:
                if open_parentheses_num == close_parentheses_num:
                    result.append(procese_parentheses)
                return
            elif open_parentheses_num > n or close_parentheses_num > n:
                return
            
            if open_parentheses_num == close_parentheses_num:
                addParentheses(open_parentheses_num + 1, close_parentheses_num, procese_parentheses + "(")
            elif open_parentheses_num > close_parentheses_num:
                addParentheses(open_parentheses_num + 1, close_parentheses_num, procese_parentheses + "(")
                addParentheses(open_parentheses_num, close_parentheses_num + 1, procese_parentheses + ")")
        addParentheses(open_parentheses_num, close_parentheses_num, procese_parentheses)

        return result

### 3rd - 2
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        process_parentheses = "("

        open_parentheses_num = 1
        close_parentheses_num = 0

        def addParentheses(open_parentheses_num, close_parentheses_num, process_parentheses):
            if len(process_parentheses) == 2 * n:
                if open_parentheses_num == close_parentheses_num:
                    result.append(process_parentheses)
                return
            elif open_parentheses_num > n or close_parentheses_num > n:
                return
            
            if open_parentheses_num == close_parentheses_num:
                addParentheses(open_parentheses_num + 1, close_parentheses_num, process_parentheses + "(")
            elif open_parentheses_num > close_parentheses_num:
                addParentheses(open_parentheses_num + 1, close_parentheses_num, process_parentheses + "(")
                addParentheses(open_parentheses_num, close_parentheses_num + 1, process_parentheses + ")")
        addParentheses(open_parentheses_num, close_parentheses_num, process_parentheses)
        return result


### 3rd - 3
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        procese_parentheses = "("

        open_parentheses_num = 1
        close_parentheses_num = 0
        
        def add_parentheses(open_parentheses_num, close_parentheses_num, procese_parentheses):
            if len(procese_parentheses) == 2 * n:
                if open_parentheses_num == close_parentheses_num:
                    result.append(procese_parentheses)
                return
            elif open_parentheses_num > n or close_parentheses_num > n:
                return
            
            if open_parentheses_num == close_parentheses_num:
                add_parentheses(open_parentheses_num + 1, close_parentheses_num, procese_parentheses + "(")
            elif open_parentheses_num > close_parentheses_num:
                add_parentheses(open_parentheses_num + 1, close_parentheses_num, procese_parentheses + "(")
                add_parentheses(open_parentheses_num, close_parentheses_num + 1, procese_parentheses + ")")
            
        add_parentheses(open_parentheses_num, close_parentheses_num, procese_parentheses)
        return result

# 時間がなくてためせてないが、defを定義せずに実装してる方法もあるのでこの方法でも実装しておきたい。(4thとかの課題)
