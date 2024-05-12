
## 1st
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # ぱっと思いついたのは、先頭から見ていって、見ているもの以外に同じものがあればスキップ、なければそのindexを返す。
        # 5分くらい考えたがこの方法しか思いつかなかったのでいったん実装する。

        index = 0
        while index < len(s):
            word = s[index]
            if word not in s[:index]+s[index+1:]:
                return index
            index += 1
        return -1

# 15 分くらいかかった。最初はfor文でやろうとしたり、indexをどう扱うかなど、いろいろ考えるのに時間がかかった。
# Runtime 1126 m, Memory 17.02 MB なのでめちゃめちゃ遅い。<- while で n回、ifのところでn回 == O(n^2)になってるので遅い
# 全体を一回見るだけにできそうだが、ぱっと思いつかないのでいろいろ見てく.


## 2nd 
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # 以下参考。
        # https://leetcode.com/problems/first-unique-character-in-a-string/solutions/4678472/for-beginners-easy-and-simple/?envType=list&envId=xo2bgr0r
        # Time complexity: O(n)
        # Space complexity: O(n) (for java and pyhton), O(1) for cpp

        dicts = defaultdict(int)

        for char in s:
            dicts[char]+=1

        # python3.7以降ではdictのkeyの順番が保証されるようだ.
        # https://docs.python.org/3/whatsnew/3.7.html
        for index in range(len(s)):
            if dicts[s[index]] == 1:
                return index
        return -1

# for 文を二回やってるので、O(2n)==O(n)である。時間計算量はよくなってるが、空間計算量としてはdictsに保存されるのでO(n)必要になってる。
# 117ms, 16.98MB


# 以下を参考にしたバージョン
#https://github.com/hayashi-ay/leetcode/pull/28/files

# ダブってないものは dict に追加して、ダブった character は dict から取り除いておく。最後に、dict に最初に追加した index を返す == ダブってないなかでもっとの小さい index になる。

class Solution:
    def firstUniqChar(self, s: str) -> int:

        dicts = {}
        upper_bond = 10**5
        duplicated = set()

        for index, char in enumerate(s):
            if char in duplicated:
                continue
            if char in dicts:
                del dicts[char]
                duplicated.add(char)
                continue
            dicts[char] = index
        if not dicts.values():
            return -1
        return next(iter(dicts.values()))

#時間計算量は O(n) <- 2n よりも短い。空間計算量はdictsとduplicated合わせてO(n)かな。<-少し自信ないが合わせてnになるはず.

