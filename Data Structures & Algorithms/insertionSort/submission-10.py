# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        ret = []
        print(len(pairs))
        if (len(pairs) == 0):
            return pairs
        if (len(pairs) == 1):
            ret.append(pairs[:])
            return ret

        for i in range (0, len(pairs) - 1):
            ret.append(pairs[:])
            if pairs[i + 1].key < pairs[i].key:
                j = i
                while (j >= 0 and pairs[j + 1].key < pairs[j].key):
                    tmp = pairs[j + 1]
                    pairs[j + 1] = pairs[j]
                    pairs[j] = tmp
                    j -= 1
        ret.append(pairs[:])
        return ret
                