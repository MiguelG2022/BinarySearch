# BinarySearch

Welcome to the Binary Search problems repository! In this repository, you will find a variety of problems that can be solved using variations of the binary search algorithm. All the solutions are provide in Python. 

Binary search is an efficient search algorithm that works by repeatedly dividing a sorted list in half to narrow down the search for a specific value.

To get started, you will need a basic understanding of how the binary search algorithm works. Here is a brief overview:

1. Begin by setting the lower and upper bounds of the list you are searching to the first and last elements of the list, respectively.

2. Calculate the midpoint of the list by taking the average of the lower and upper bounds.

3. If the value you are searching for is greater than the value at the midpoint, set the lower bound to the midpoint + 1 and repeat the process from step 

4. If the value you are searching for is less than the value at the midpoint, set the upper bound to the midpoint - 1 and repeat the process from step

5. If the value you are searching for is equal to the value at the midpoint, you have found the value and can stop the search.

6. If the lower bound becomes greater than the upper bound, the value you are searching for is not present in the list and the search can be stopped.


```
def binarySearch(nums, target):
    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = (start+end)//2
        if arr[mid] < target:
            start = mid + 1
        elif arr[mid] > target:
            end = mid -1 
        else:
            return mid 
    return -1 
```

https://leetcode.com/problems/binary-search/ Easy 

https://leetcode.com/problems/find-smallest-letter-greater-than-target/solutions/?orderBy=most_votes Easy 

https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/ Medium 

https://www.geeksforgeeks.org/find-position-element-sorted-array-infinite-numbers/ Medium 

https://leetcode.com/problems/peak-index-in-a-mountain-array/description/ Medium 

https://leetcode.com/problems/search-in-rotated-sorted-array/description/ Medium 

https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/description/ Hard

https://leetcode.com/problems/split-array-largest-sum/ Hard 
