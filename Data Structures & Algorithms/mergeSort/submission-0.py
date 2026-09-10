# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) <= 1:
            return pairs
        
        mid = len(pairs) // 2

        # Sort Left 
        left = self.mergeSort(pairs[:mid])
        
        # Sort Right
        right = self.mergeSort(pairs[mid:])

        return self.merge(left, right)

    def merge(self, left, right):
        sorted_arr = []
        i = 0
        j = 0

        while i < len(left) and j < len(right):
            if left[i].key <= right[j].key:
                sorted_arr.append(left[i])
                i += 1
            else:
                sorted_arr.append(right[j])
                j += 1            

        sorted_arr.extend(left[i:])
        sorted_arr.extend(right[j:])
        
        return sorted_arr
            

