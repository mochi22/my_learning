## 1st

#以下の方針が立ったが、全くコードが書けなかった。
"""
以下の条件なので、n 個の candidates を全てのパターンを計算すればよさそう。
-> 単純にwhileとfor文を使えばかけそうだし、再帰関数を使ってかけそう。

- 1 <= candidates.length <= 30
- 2 <= candidates[i] <= 40
- All elements of candidates are distinct.
- 1 <= target <= 40

-> うまく実装できなかった。
"""


## 2nd

"""
いろいろな解答見たが、コードに慣れていないのもあって、納得する回答が見つからず、数時間浪費してしまった。

一旦以下を見つつ、時間をかけて自分なりの回答を作成していく。
https://github.com/SuperHotDogCat/coding-interview/pull/11/files


具体的には以下の思考をコードにしていく。
candidatesが小さいものから一つずつ追加していく。和がtargetを超えたら追加を終了する。
(条件に記載はないが、candidatesがソート済みで、小さいものから追加するのと大きいものから追加するのは同じ探索数になる)
-> sort済みではなかった。。。
sortしない場合の計算量は O(n+nC2) ~= O(n^2) <- stackに入れるので O(n)、すべての組み合わせでO(nC2)
sortして、打ち切りする場合の計算量は、O(nlogn + n + nC2 / 2) ~= O(n^2) <- sortで O(nlogn)、stackに入れるので O(n)、すべての組み合わせの内新規で小さいものを入れない場合は半分になるはずなのでO(nC2 / 2) <= ぱっと半分になると思ったが、よくよく考えたらもっと減るかも
-> 計算量的にsortしてもしなくてもそんな変わらない。(というか n が小さいので、まだ気にしなくてもよい)
取り出すときは小さいものから取り出したいのでキューで取り出す。

ex) candidaes = [2,3,6,7], target = 7
[] -> [[2],[3],[6],[7]]

[[2],[3],[6],[7]] -> [[2,2],[2,3],[2,6],[2,7]...] 

"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []
        stack = []

        for index in range(len(candidates)):
            stack.append([index, []])

        while stack:

            # こっから追加処理
            current_process = stack.pop(0)

            current_index = current_process[0]
            if current_index >= len(candidates):
                continue
            # mutable なので copy しとく
            current_combination = current_process[1].copy()
            current_combination.append(candidates[current_index])

            sum_current_process = sum(current_combination)
            
            # ここから条件
            if sum_current_process == target:
                # mutable なのでcopyつけて、result に追加
                result.append(current_combination)
                continue
            elif sum_current_process > target:
                # target 超えたので探索打ち切り
                continue
            elif sum_current_process < target:
                # 追加していく
                for i in range(len(candidates)):
                    if current_index + i < len(candidates):
                        stack.append([current_index + i, current_combination])
                
        
        return result
    
# sort したバージョンは以下・
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []
        stuck = []

        candidates.sort()

        for index in range(len(candidates)):
            stuck.append([index, []])

        while stuck:

            # こっから追加処理
            current_process = stuck.pop(0)

            current_index = current_process[0]
            if current_index >= len(candidates):
                continue
            # mutable なので copy しとく
            current_combination = current_process[1].copy()
            current_combination.append(candidates[current_index])

            sum_current_process = sum(current_combination)
            
            # ここから条件
            if sum_current_process == target:
                # mutable なのでcopyつけて、result に追加
                result.append(current_combination)
                continue
            elif sum_current_process > target:
                # target 超えたので探索打ち切り
                continue
            elif sum_current_process < target:
                # 追加していく
                for i in range(len(candidates)):
                    if current_index + i < len(candidates) and current_combination[-1] <= candidates[current_index + i]:
                        stuck.append([current_index + i, current_combination])
                
        
        return result