"""
Sorting algorithms with optimization flags.
"""

def quicksort(arr, optimize=True):
    """QuickSort with median-of-three pivot selection."""
    if len(arr) <= 1:
        return arr
    
    if optimize:
        pivot = _median_of_three(arr)
    else:
        pivot = arr[len(arr) // 2]
    
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quicksort(left, optimize) + middle + quicksort(right, optimize)


def _median_of_three(arr):
    """Return median of first, middle, last elements."""
    first, mid, last = arr[0], arr[len(arr)//2], arr[-1]
    return sorted([first, mid, last])[1]
