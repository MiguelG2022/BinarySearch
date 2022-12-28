#Hello in this file you will find a list of problems where one can use binary search to solve the problem
# Standard Form of Binary Search, Binary search takes in an input array with a list of values in sorted order and returns the index of the value if it exists 
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



# look at ceiling of a number which is the smallest elemenet greater than or equal to the target 
# see sorted arrray do binary search
# arr = [2,3,5,9,14,16,18], target 14

def find_ceiling(nums,target):
    start = 0
    end = len(nums) - 1 

    while start <= end:
        mid = (start+end)//2

        if nums[mid] > target:
            end = mid - 1
        elif nums[mid] < target:
            start = mid + 1
        else:
            return nums[mid] 
    
    return start 

nums = [2,3,5,9,14,16,18]
print(find_ceiling(nums,16)) # 16
print(find_ceiling(nums,4)) # 5
print(find_ceiling(nums,10)) # 14
print(find_ceiling(nums,19))

# look at floor of a number which is the smallest elemenet greater than or equal to the target 

def find_floor(nums,target):
    start = 0
    end = len(nums) - 1 
    
    while start <=end:
        mid = (start+end) // 2 
        if nums[mid] > target:
            end = mid -1 
        elif nums[mid] < target:
            start = mid + 1
        else:
            return nums[mid]

    return end

print("-------------------------")
print(find_floor(nums,16)) # 16
print(find_floor(nums,4)) # 3
print(find_floor(nums,10)) # 9
print(find_floor(nums,19)) #6

# start and end pointer mean the target is between the two pointers, minimzing the search space, answer lies in between. when start is greater than end, it means answer lies between those two pointers, depending on what you are looking for you are going to use the start or end pointer. the end pointer is the position where the answer should have gone or cieling of that value 


#https://leetcode.com/problems/find-smallest-letter-greater-than-target/solutions/?orderBy=most_votes
# Exact same approach as ceiling except few caveats. Ignore the equal part

print("-------------------------")
print("a">"b")

def nextGreatestLetter(letters,target):
    start = 0 
    end = len(letters)-1
    while start<=end:
        mid = (start+end)//2
        if letters[mid] > target:
            end = mid - 1 
        else:
            start = mid + 1 
    return letters[start%len(letters)]

letters= ["a","g","g"]
print(nextGreatestLetter(letters, "g"))


# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# find the first and last position of element in sorted index 

print("-------------------------")

def searchRange(nums, target):
    res = [-1,-1]
    res[0] = helperSearchRange(nums,target,False)
    res[1] = helperSearchRange(nums,target,True)
    return res 

def helperSearchRange(nums,target,last):
    start = 0
    end = len(nums) - 1 
    res = -1 
    while start <= end:
        mid = (start+end)//2
        if nums[mid] > target: 
            end = mid -1 
        elif nums[mid] < target:
            start = mid + 1 
        else:
            res = mid 
            if last:
                start = mid + 1
            else:
                end = mid - 1 
    return res 

                
nums = [5,7,7,8,8,10]
target = 8
print(searchRange(nums, target))
# Output: [3,4]
Input: nums = [5,7,7,8,8,10]
target = 6
print(searchRange(nums, target))
# Output: [-1,-1]




# Find position of an element in a sorted array of infinite numbers
# start bottom up, see if target is between start and end, double each time, then see if it's right 
# https://www.geeksforgeeks.org/find-position-element-sorted-array-infinite-numbers/

def infinityArray(nums, target):
    # first find the range
    start = 0
    end = 1 
    # condition for the target to lie in range, target is less than end 
    while target > nums[end]:
        newStart = end + 1
        #double box value, end is equal to previous end + size of box * 2 
        end = end + (end-start+1) * 2 
        start = newStart
    
    return helperInfinityArray(nums, target, start, end)


def helperInfinityArray(nums, target, start, end):
    while start <= end:
        mid = (start+end) // 2

        if nums[mid] > target:
            end = mid - 1 
        elif nums[mid] < target:
            start = mid + 1
        else:
            return mid 

# https://leetcode.com/problems/peak-index-in-a-mountain-array/description/
# [1,2,3,5,6,4,3,2]

print("-------------------------")
def peakIndex(nums):
    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = (start + end)//2
        if nums[mid] > nums[mid+1]:
            res = mid
            end = mid-1
        else:
            start = mid + 1 
    return nums[res] 

def peakIndexPartTwo(nums):
    start = 0
    end = len(nums) - 1
    while start < end:
        mid = (start+end)//2
        if nums[mid] > nums[mid+1]:
            end = mid 
        else:
            start = mid + 1 
    return nums[end] 
nums = [1,2,3,5,6,4,3,2] 
print(peakIndex(nums))
print(peakIndexPartTwo(nums))
#output: 6

# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
# one way is to find pivot and then run binary search on two sections 
# cases for pivot, mid element is greater than mid + 1 then that is pivot, case 2 mid is less than mid -1 element that is pivot. if start element is greater than mid element, end = mid - 1 
# last case if start element is smaller than mid element, than start = mid + 1 


def findPivot(nums):
    start = 0 
    end = len(nums)-1
    while start<=end:
        mid = (start+end)//2
        if mid < end and arr[mid] > arr[mid+1]:
            return mid 
        if mid > start and arr[mid] < arr[mid-1]:
            return mid - 1
        if arr[mid] <= arr[start]:
            end = mid -1 
        else:
            start = mid +1 
    return -1 

def findPivotWithDuplicates(arr):
    start = 0 
    end = len(arr)-1
    while start<=end:
        mid = (start+end)//2
        if mid < end and arr[mid] > arr[mid+1]:
            return mid 
        if mid > start and arr[mid] < arr[mid-1]:
            return mid - 1
        #if elements at middle, start and end are equal, then skip the duplicates 
        if arr[mid] == arr[start] and arr[mid] == arr[end]:
            #skip all duplicates, but what if they were the pivots
            if arr[start] > arr[start+1]:
                return start 
            start += 1
            if arr[end] < arr[end-1]:
                return end - 1
            end -= 1
        elif arr[start] < arr[mid] or (arr[start] == arr[mid] and arr[mid] > arr[end]):
            start = mid + 1
        else:
            end = mid - 1
    return -1 

print(findPivotWithDuplicates([2,2,3,0,]))


# find min in rotatated sorted array 2 https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/description/
def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pivot = self.findPivot(nums)
        if pivot==-1:
            return nums[0]
        else:
            return nums[pivot+1]

    
def findPivotRSA(self, nums):
    start = 0 
    end = len(nums)-1
    while start<=end:
        mid = (start+end)//2
        if mid < end and nums[mid] > nums[mid+1]:
            return mid 
        if mid > start and nums[mid] < nums[mid-1]:
            return mid - 1 
        if nums[mid] == nums[start] and nums[mid] == nums[end]:
            if start+1 < end and nums[start] > nums[start+1]:
                return start 
            start += 1
            if nums[end] < nums[end-1]:
                return end-1
            end -= 1 
        elif nums[mid] == nums[start] or nums[mid]>nums[start]:
            start = mid + 1
        else:
            end = mid -1 
    return -1 
# find how many times a arrary is rotated 
# [4,5,6,7,0,1,2] it is rotated pivot times 

def countRotations(arr):
    start = 0
    end = len(arr)-1
    while start<=end:
        mid = (start + end) //2
        if mid < end and arr[mid] > arr[mid+1]:
            return mid + 1
        if mid > start and arr[mid] < arr[start-1]:
            return mid 
        if arr[mid] <= arr[start]:
            mid = end - 1
        else:
            end = mid + 1
    return 0 
arr = [4,5,6,7,0,1,2]
print(countRotations(arr))


# split arrray largest sum https://leetcode.com/problems/split-array-largest-sum/

arr = [7,2,5,10,8] 
m = 2 

# can split it in two non empty continous sub arrays 
# min number of split is 1 and max is length of array 
# in case one it is the sum of array 
# only one way to split it length of array times 
# sum of entire array is max, min is max element in array 
# range of max answer and min answer 
# [10, 32] 10 is lower limit highest limit 

# middle is 21m see if you can split the array with 21 as the max sum 
# can split into 2 pieces 
# if pieces <= m, end = mid
# mid = 15, 10 + 21//2 
# pieces = 3 <=m, start = mid + 1 
# 16 + 21 // 2 = 18 = mid 
# start = 16, end = 18,
# new mid 17 3 pieces
# start = mid + 1
# start 18 and end = 18 


def splitArray(nums, m):
    start = max(nums)
    end = sum(nums)
    
    while start < end:
        mid = (start+end) // 2
        # calculate how many pieces you can divide this in with max sum
        total = 0
        pieces = 1 
        for num in nums:
            if total+num > mid:
                # you can not add this to subarray
                pieces+=1
                total = num
            else:
                total += num 
        
        if pieces > m:
            start = mid + 1
        else:
            end = mid 
    
    return end 

