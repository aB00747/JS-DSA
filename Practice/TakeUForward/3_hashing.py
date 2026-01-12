# elements = [1, 2, 2, 3, 1, 4, 2]
# for index, value in enumerate(elements):
#     print(f"Index: {index}, Value: {value}")


# Count frequency
# 1. Count the frequency of the element in a list
def countFreq(arr):
    freq = {}

    for item in arr:
        print(item)
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    
    return freq

element = [1, 2, 2, 3, 1, 4, 2]
print(countFreq(element))

# Find the highest freq
def highFreq(arr):
    freq = {}

    for item in arr:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return max(freq.values())


print("highest freq", element,  "->", highFreq(element))

# 3005. Count Elements With Maximum Frequency
# You are given an array nums consisting of positive integers.
# Return the total frequencies of elements in nums such that those elements all have the maximum frequency.
# The frequency of an element is the number of occurrences of that element in the array.

# Example 1:
# Input: nums = [1,2,2,3,1,4]
# Output: 4
# Explanation: The elements 1 and 2 have a frequency of 2 which is the maximum frequency in the array.
# So the number of elements in the array with maximum frequency is 4.

# Example 2:
# Input: nums = [1,2,3,4,5]
# Output: 5
# Explanation: All elements of the array have a frequency of 1 which is the maximum.
# So the number of elements in the array with maximum frequency is 5.

from collections import Counter

def maxFrequencyElements(nums):
    freq = Counter(nums)

    max_freq = max(freq.values())

    total = 0
    for count in freq.values():
        if count == max_freq:
            total += count

    return total

print("maxFrequencyElements", maxFrequencyElements(element))

# without pre-defined [ACCEPTED ON LEETCODE]
def maxFrequencyElements2(nums):
    freq = {}

    for item in nums:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    
    max_freq = max(freq.values())
    print("max_freq", max_freq, "values", freq.values())

    total = 0
    for count in freq.values():
        if count == max_freq:
            total += count

    return total

print("maxFrequencyElements2", maxFrequencyElements2(element))

