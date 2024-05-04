
## 1st
# 30分くらいかけて brute force で回答。
# 回答後に nums がユニークだと気付いた。(条件を書いたのに見落としていた。)


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        """
        入力された配列のすべての順列の組み合わせを求める。提出の順番は何でもよい。

        条件は以下。
        1 <= nums.length <= 6
        -10 <= nums[i] <= 10    
        All the integers of nums are unique.

        -> nums.lengthが6以下なので、全探索でよさそう。再帰関数でもできそうだけど簡単に実装できるbrute forceで回答する。
        具体的には、i 番目の要素を nums.length だけ list に追加して、ユニークな列を最後に提出する
        """
        length = len(nums)
        if length == 1:
            return [nums]

        processing_index_list = []
        processing_list = []
        for index in range(length):
            processing_index_list.append([index])
            processing_list.append([nums[index]])


        result = []
        index_result = []

        while processing_index_list:
            tmp_index_list = processing_index_list.pop(0)
            tmp_list = processing_list.pop(0)

            for current_index in range(length):
                
                if current_index in tmp_index_list:
                    continue
                current_tmp_index_list = tmp_index_list.copy()
                current_tmp_index_list.append(current_index)
                current_tmp_list = tmp_list.copy()
                current_tmp_list.append(nums[current_index])

                # length 以下なら追加する
                if len(current_tmp_index_list) < length:
                    processing_index_list.append(current_tmp_index_list)
                    processing_list.append(current_tmp_list)
                # 終了条件
                elif len(current_tmp_index_list) == length:
                    if not current_tmp_index_list in index_result:
                        result.append(current_tmp_list)
                        index_result.append(current_tmp_index_list)
  
        return result


## 2nd 
#参考: https://qiita.com/ccc79783379/items/efbbdd7f3999c8806b55
# 明らかに再帰関数で書く方が楽
# permutation というのは 順列 を意味する。

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 考え方としては、nums のものを一つずつ process_list に加えるか考えて、長さが nums と同じになったら result に追加する。
        # 一つずつ追加する方法は for 分の中で 関数を呼ぶ。

        result = []


        def backtrack(process_list : List[int]) -> List[List[int]]:

            # 条件(関数呼び出して判定してから、追加処理を行いたいので最初に条件)
            if len(process_list) == len(nums):
                result.append(process_list.copy())

            # 追加処理
            for num in nums:
                if not num in process_list:
                    process_list.append(num)
                    backtrack(process_list)
                    # これで一つ戻る
                    process_list.pop()
        
        backtrack([])
        return result
    

## 3rd - 1
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(process_list: List[int]) -> List[List[int]]:
            
            if len(process_list) == len(nums):
                result.append(process_list.copy())

            for num in nums:
                if not num in process_list:
                    process_list.append(num)
                    backtrack(process_list)
                    process_list.pop()

        
        backtrack([])
        return result


## 3rd - 2
# 再帰関数の名前をcheck_all_permutationsと意味のある名前にした。
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        result = []

        def check_all_permutations(process_list: List[int]) -> List[List[int]]:
            if len(process_list) == len(nums):
                result.append(process_list.copy())
            for num in nums:
                if not num in process_list:
                    process_list.append(num)
                    check_all_permutations(process_list)
                    process_list.pop()

        check_all_permutations([])
        return result



## 3rd - 3
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        def check_all_permutations(process_list : List[int]) -> List[List[int]]:
            if len(process_list) == len(nums):
                result.append(process_list.copy())
            for num in nums:
                if not num in process_list:
                    process_list.append(num)
                    check_all_permutations(process_list)
                    process_list.pop()
                
        check_all_permutations([])
        return result