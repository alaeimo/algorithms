
class Sort:
    def __init__(self):
        pass

    @staticmethod
    def bubble_sort(arr, ascending=True):
        for i in range(len(arr)):
            swapped = False
            for j in range(len(arr)-i-1):
                if ascending and arr[j] > arr[j+1] or not ascending and arr[j] < arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True
            if not swapped:
                break
        return arr
    @staticmethod
    def selection_sort(arr, ascending=True):
        for i in range(len(arr)):
            minmax_idx = i
            for j in range(i+1,len(arr)):
                if ascending and arr[j] < arr[minmax_idx] or not ascending and arr[j] > arr[minmax_idx]: 
                    minmax_idx = j
            arr[i], arr[minmax_idx] = arr[minmax_idx], arr[i]
        return arr
    @staticmethod
    def insertion_sort(arr, ascending=True):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j>=0 and key < arr[j]:
                arr[j+1] = arr[j]
                j = j - 1
            arr[j+1] = key
        return arr

    @staticmethod
    def merge(L, R):
        sorted_arr = [None] * (len(L)+ len(R))
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                sorted_arr[k] = L[i]
                i += 1
            else:
                sorted_arr[k] = R[j]
                j += 1
            k += 1
        if i < len(L):
            sorted_arr[k:] = L[i:]
        if j < len(R):
            sorted_arr[k:] = R[j:]
        return sorted_arr
    @staticmethod
    def merge_sort(arr):
        if len(arr) <= 1:return arr
        q = len(arr)//2
        L = arr[:q]
        R = arr[q:]

        L = Sort.merge_sort(L)
        R = Sort.merge_sort(R)
        return Sort.merge(L, R)

    @staticmethod
    def partition(arr):
        i = -1
        pivot = arr[-1]
        for j in range(len(arr) - 1):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[-1] = arr[-1], arr[i+1]
        return i+1
    @staticmethod
    def quick_sort(arr):
        if len(arr)<= 1: return arr
        pivot = Sort.partition(arr)
        left_arr = Sort.quick_sort(arr[:pivot])
        right_arr = Sort.quick_sort(arr[pivot:])
        return left_arr + right_arr