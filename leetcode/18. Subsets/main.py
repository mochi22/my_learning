
## 1st
# set 使えば、順序を考慮しなくて済みそうだと考えたが、探索時の順序が壊れて正しく探索されない。
# 10 分くらい考えてもよさそうな方法が思いつかず失敗。
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        # #ユニークな値が与えられており、ユニークな組み合わせをreturnする。
        
        # # 再帰的にそれぞれの要素をユニークならlistに追加する
        # # Permutations と同じようなコードで行けそうだけど、並び順が異なる組み合わせは一つにしたい。
        # # -> 順番が異なるものも一つだけにしたいので、setを使う

        result = [[]]
        process_list = set()
        def make_subsets(process_list, result):
            for num in nums:
                if num not in process_list:
                    process_list.add(num)
                    if process_list not in result:
                        result.append(process_list.copy())
                    make_subsets(process_list, result)
                    
                    process_list.pop()
        
        make_subsets(process_list, result)

        return result


## 2nd
# chatgptに聞いた。変数名などは修正した。
# index を使えば、探索済みのユニークな num は process_list に追加されず、ユニークな組み合わせのみになる。
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result = []
    
        def make_subsets(index : int, process_list: List[int]) -> List[int]:
            # 現在の経路を結果に追加
            result.append(process_list.copy())
            
            # 部分集合を生成するために再帰的に探索
            # index を一つずつ増やすことで、探索済みの場所は再度探索されない
            for current_index in range(index, len(nums)):
                process_list.append(nums[current_index])
                make_subsets(current_index + 1, process_list)
                process_list.pop()
        
        make_subsets(0, [])
        return result
    


## 3rd - 1

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result = []

        def make_subsets(index, process_list):

            result.append(process_list.copy())

            for current_index in range(index, len(nums)):
                process_list.append(nums[current_index])
                make_subsets(current_index + 1, process_list)
                process_list.pop()
            
        make_subsets(0, [])

        return result


## 3rd - 2
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result = []

        def make_subsets(index, process_list):

            result.append(process_list.copy())

            for current_index in range(index, len(nums)):
                process_list.append(nums[current_index])
                make_subsets(current_index + 1, process_list)
                process_list.pop()
            
        make_subsets(0, [])

        return result
    


## 3rd - 3
# 再帰関数も type hint を追加した。
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = []

        def make_subsets(index: int, process_list: List[int]) -> None:
            result.append(process_list.copy())
            for current_index in range(index, len(nums)):
                process_list.append(nums[current_index])
                make_subsets(current_index + 1, process_list)
                process_list.pop()
        make_subsets(0, [])

        return result
    

# train_credit_bureau_a_1
# train_static_0
# train_person_1

# train_static_cb_0
# train_applprev_1