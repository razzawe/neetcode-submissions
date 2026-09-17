class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        largest = 0
        for i in range(len(arr)-1, -1, -1):
            if i == len(arr)-1:
                largest = arr[i]
                arr[i] = -1
        
            elif arr[i] > largest:
                temp = largest
                largest = arr[i]
                arr[i] = temp
            else: 
                arr[i] = largest
        return arr

