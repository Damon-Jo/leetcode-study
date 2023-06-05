# Given an array arr,
# replace every element in that array with the greatest element among the elements to its right,
# and replace the last element with -1.
# After doing so, return the array.

class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:

        #arr = [17,18,5,4,6,1]   1 6 4 5 18 17
        #sored arr = [18 17 6 5 4 1]

        arr = arr[::-1]
        result = []
        max_numb = -1

        for i in arr :
            result.append(max_numb)

            if max_numb < i:
                max_numb = i

        return result[::-1]