
def constantWindow(arr, k):
    """
    Find the maximum sum of a contiguous subarray of fixed size k using the sliding window technique.
    This function uses a sliding window approach with O(n) time complexity to efficiently
    calculate the maximum sum of any consecutive k elements in the array.
    Args:
        arr (list): A list of integers that may contain positive and negative numbers.
        k (int): The size of the window (number of consecutive elements to consider).
    Returns:
        int: The maximum sum found among all contiguous subarrays of size k.
    Example:
        >>> constantWindow([-1, 2, 3, 3, 4, 5, -1], 4)
        15
        The subarray [3, 3, 4, 5] has the maximum sum of 15.
    Time Complexity:
        O(n) where n is the length of the array.
    Space Complexity:
        O(1) - only uses constant extra space.
    """

    l = 0
    r = k - 1
    n = len(arr)
    windowSum = 0
    for i in range(l, k):
        windowSum += arr[i]
    # windowSum = sum(arr[:k])

    max_window = windowSum

    while r < n - 1:
        windowSum = windowSum - arr[l]
        l += 1
        r += 1

        windowSum = windowSum + arr[r]
        max_window = max(max_window, windowSum)

    return max_window

element = [-1, 2, 3, 3, 4, 5, -1]
consecutive_k = 4
# print(constantWindow(element, consecutive_k))


# Longest subarray/substring where <condition>

# Longest subarray with sum <= k
def longestSubarry(arr, k):
    """
    Find the length of the longest subarray with a sum less than or equal to k.
    This function uses a sliding window approach with two pointers to efficiently
    find the longest contiguous subarray whose sum does not exceed the given value k.
    Args:
        arr (list): A list of integers representing the array to search.
        k (int): The maximum sum threshold for the subarray.
    Returns:
        int: The length of the longest subarray with sum <= k. Returns 0 if no
             such subarray exists.
    Time Complexity:
        O(n) where n is the length of the array. Each element is visited at most
        twice (once by right pointer, once by left pointer).
    Space Complexity:
        O(1) as only a constant amount of extra space is used.
    Example:
        >>> longestSubarry([1, 2, 3, 4, 5], 10)
        4
        >>> longestSubarry([2, 2, 2, 2], 5)
        2
    """

    maxLen = 0
    # l = 0
    # r = 0
    # sum = 0
    l = r = sum = 0
    n = len(arr)

    while r < n - 1:
        sum = sum + arr[r]

        while k < sum:
            sum = sum - arr[l]
            l += 1
        
        maxLen = max(maxLen, (r - l) + 1)
        r += 1
    
    return maxLen


def longestSubarrayOptimise(arr, k):
    """
    Find the length of the longest subarray with sum less than or equal to k.
    This function uses a two-pointer sliding window approach to efficiently find
    the longest contiguous subarray whose sum does not exceed a given value k.
    Args:
        arr (list): A list of integers representing the array to search.
        k (int): The maximum sum threshold for valid subarrays.
    Returns:
        int: The length of the longest subarray with sum <= k.
    Time Complexity:
        O(n) - where n is the length of the input array. Each element is visited
        at most twice (once by right pointer, once by left pointer).
    Space Complexity:
        O(1) - only constant extra space is used for variables.
    Example:
        >>> longestSubarrayOptimise([1, 2, 3, 1, 1, 1], 3)
        3
        >>> longestSubarrayOptimise([8, 2, 5, 1, 2, 5], 10)
        2
    """

    maxLen = l = r = sum = 0
    n = len(arr)

    while r < n:
        sum = sum + arr[r]

        if sum > k:
            sum = sum - arr[l]
            l += 1

        if sum <= k:
            maxLen = max(maxLen, r - l + 1)

        r += 1

    return maxLen

arr1 = [2, 5, 1, 7, 10]
# print(longestSubarry(arr1, 14))
# print(longestSubarrayOptimise(arr1, 14))


# you can pick the card form left or right side not from the middle k - how much cards are
def maxPointsCard(arr, k):
    """
    Find the maximum sum of k cards taken from either end of an array.
    This function uses a sliding window approach with two pointers to calculate
    the maximum sum that can be obtained by taking k cards from the beginning
    and/or end of the array.
    Args:
        arr (list): A list of integers representing the card values.
        k (int): The number of cards to select from the array.
    Returns:
        int: The maximum sum obtainable by selecting k cards from either end
             of the array.
    Raises:
        IndexError: If k is greater than the length of arr.
    Example:
        >>> maxPointsCard([1, 2, 3, 4, 5], 2)
        9  # Taking 5 and 4 from the right end
        >>> maxPointsCard([8, 1, 2, 3, 5], 2)
        13  # Taking 8 from left and 5 from right
    Time Complexity:
        O(k) - The algorithm iterates k times to slide the window.
    Space Complexity:
        O(1) - Only uses constant extra space for variables.
    """

    l = k - 1
    n = len(arr)
    r = n - 1
    maxSum = sumArr = sum(arr[:k])

    while l >= 0:
        # sum += arr[l]
        sumArr -= arr[l]
        l -= 1

        sumArr += arr[r]
        r -= 1

        print("sumArr", sumArr)

        maxSum = max(maxSum, sumArr) 

    return maxSum

arr2 = [6, 2, 3, 4, 7, 2, 1, 7, 1]
# print(maxPointsCard(arr2, 4))


def uniqueSubstring(str):
    """
    Finds the length of the longest substring without repeating characters.
    This function iterates through the input string and counts consecutive
    characters until it encounters a character that has already been seen.
    It returns the count of unique characters found before any repetition.
    Args:
        str (str): The input string to analyze.
    Returns:
        int: The length of the longest substring with all unique characters
             starting from the beginning of the string.
    Example:
        >>> uniqueSubstring("abcabcbb")
        3
        >>> uniqueSubstring("bbbbb")
        1
        >>> uniqueSubstring("pwwkew")
        3
    Note:
        This implementation only captures the longest substring from the start.
        For a more general solution that finds the longest substring anywhere
        in the string, consider using a sliding window approach with two pointers.
    """

    hashing = []
    # n = len(str)
    count = 0

    # for i in range(n - 1):
    for char in str:
        # if str[i] in hashing:
        if char in hashing:
            break

        # hashing.append(str[i])
        hashing.append(char)
        count += 1

    return count

# print(uniqueSubstring("cadbzabcd"))


# LC 26. Remove Duplicates from Sorted Array

def removeDuplicates(nums):
    if not nums:
        return 0
    
    i = 0 # unique num

    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]

    return i + 1

nums = [0,0,1,1,1,2,2,3,3,4]
# nums = [1,1,2]
# print("removeDuplicates", removeDuplicates(nums))



# Max Consecutive Ones III
def maxOne(arr, k):
    """
    Find the maximum length of consecutive ones in an array after flipping at most k zeros.
    This function uses a sliding window approach with two pointers to find the longest
    subarray that contains at most k zeros, which when flipped would result in all ones.
    Args:
        arr (list): A list of integers containing only 0s and 1s.
        k (int): The maximum number of zeros allowed to be flipped in the subarray.
    Returns:
        int: The maximum length of consecutive ones achievable by flipping at most k zeros.
    Example:
        >>> maxOne([1, 0, 1, 1, 0], 1)
        3
        >>> maxOne([0, 0, 1, 1, 0, 0, 1], 2)
        6
    Time Complexity:
        O(n) where n is the length of the array. Both pointers traverse the array once.
    Space Complexity:
        O(1) - Only using constant extra space.
    """

    maxLen = leng = zeros = r = l = 0

    while (r < (len(arr) - 1)):
        if arr[r] == 0:
            zeros += 1

        while zeros > k:
            if arr[l] == 0:
                zeros -= 1
            l += 1

        if zeros <= k:
            leng = r - l + 1
            maxLen = max(maxLen, leng)

        r += 1

    return maxLen


nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
print("maxOne", maxOne(nums, 2)) # output: 6


# so maxOne TC is O(2n) - which can be more optimise we can reduce the 2n to n


def maxOneOptimise(arr, k):
    """
    Find the maximum length of consecutive ones in an array after flipping at most k zeros.
    Uses a sliding window (two-pointer) approach to efficiently find the longest subarray
    containing at most k zeros, which can be flipped to create consecutive ones.
    Args:
        arr (list): A list of integers containing 0s and 1s.
        k (int): Maximum number of zeros allowed to flip to ones.
    Returns:
        int: The maximum length of consecutive ones achievable after flipping at most k zeros.
    Time Complexity:
        O(n) - Single pass through the array with two pointers.
    Space Complexity:
        O(1) - Only uses a constant amount of extra space.
    Example:
        >>> maxOneOptimise([1, 0, 1, 1, 0], 1)
        3
        >>> maxOneOptimise([0, 0, 1, 1, 0, 0, 1], 1)
        3
        >>> maxOneOptimise([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2)
        6
    """

    l = r = maxLen = length = zeros = 0
    n = len(arr)

    while r < n - 1:
        if arr[r] == 0:
            zeros += 1

        if zeros > k:
            if arr[l] == 0:
                zeros -= 1
            l += 1

        if zeros <= k:
            length = r - l + 1
            maxLen = max(maxLen, length)

        r += 1

    return maxLen


print("maxOneOptimise", maxOneOptimise(nums, 2))


# Fruit into Baskets (allowed one type in one basket)
def fruitBaskets(arr, k):
    """
    Find the maximum length of a subarray containing at most k distinct elements.
    This function uses a sliding window approach with two pointers to find the longest
    contiguous subarray that contains at most k distinct fruits/elements.
    Args:
        arr (list): A list of integers representing the types of fruits.
        k (int): The maximum number of distinct fruits allowed in the basket.
    Returns:
        int: The maximum length of a subarray with at most k distinct elements.
    Example:
        >>> fruitBaskets([1, 2, 1, 2, 3], 2)
        4
        >>> fruitBaskets([0, 1, 2, 2], 2)
        3
    Time Complexity:
        O(n) where n is the length of the array. Each element is visited at most twice.
    Space Complexity:
        O(k) where k is the maximum number of distinct elements stored in the hash map.
    """

    l = 0
    r = 0
    n = len(arr)
    maxLen = 0
    mpp = {}

    while r < n:
        mpp[arr[r]] = mpp.get(arr[r], 0) + 1

        # shrink window if we have more than k distinct fruits
        while len(mpp) > k:
            mpp[arr[l]] -= 1
            if mpp[arr[l]] == 0:
                del mpp[arr[l]]
            l += 1

        # update max length
        maxLen = max(maxLen, r - l + 1)
        r += 1
    
    return maxLen


# Example test
element1 = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]
print("fruitBaskets:", fruitBaskets(element1, 2))

# subarrays with k different intergers
def diffInt(arr, k):
    l = 0
    r = 0
    n = len(arr)
    count = 0
    mpp = {}

    while r < n:
        mpp[arr[r]] = mpp.get(arr[r], 0) + 1

        # while len(mpp) > k:
        if len(mpp) > k:
            # use if instead of to reduce the TC 2n to n
            mpp[arr[l]] -= 1

            if mpp[arr[l]] == 0:
                del mpp[arr[l]]
            
            l += 1

        count += (r - l + 1)

        r += 1

    return count


arr = [2, 1, 1, 1, 3, 4, 3, 2]
print("diffInt", diffInt(arr, 3))


# Longest substring with at most k distinct characters
def longest_k_distnct(arr, k):
    """
    Find the length of the longest substring with at most k distinct characters.
    This function uses a sliding window approach with a two-pointer technique to
    efficiently find the longest contiguous substring that contains at most k
    distinct elements from the given array.
    Args:
        arr (list): A list of elements (typically integers or characters) to search through.
        k (int): The maximum number of distinct elements allowed in the substring.
    Returns:
        int: The length of the longest substring containing at most k distinct elements.
             Returns 0 if the array is empty or k is 0.
    Time Complexity:
        O(n) where n is the length of the array. Each element is visited at most twice
        (once by right pointer and once by left pointer).
    Space Complexity:
        O(min(n, k)) for the hashmap storing at most k distinct elements.
    Example:
        >>> longest_k_distnct([1, 2, 1, 2, 3], 2)
        4
        >>> longest_k_distnct(['a', 'a', 'b', 'b', 'c'], 2)
        4
    """

    l = r = 0
    max_len = 0
    mpp = {}
    n = len(arr)

    while r < n:
        mpp[arr[r]] = mpp.get(arr[r], 0) + 1

        if len(mpp) > k:
            mpp[arr[l]] = mpp.get(arr[l], 0) - 1

            # delete hash key and value
            if mpp[arr[l]] == 0:
                del mpp[arr[l]]

            l += 1

        if len(mpp) < k:
            max_len = max(max_len, r - l + 1)

        r += 1

    return max_len

s = "aaabbccd"
print("longest_k_distnct", longest_k_distnct(s, 2))


# Number of substrings Containig all three characters
def rough_num_substring_three_char(s):
    count = 0
    n = len(s)

    for i in range(n):
        char_hash = {}

        for j in range(i, n):
            char_idx = ord(s[j]) - ord('a')
            if char_idx < 3:  # only count 'a', 'b', 'c'
                char_hash[char_idx] = 1

            if len(char_hash) == 3:
                count += 1

    return count

s = "bbacba"
print(rough_num_substring_three_char(s))


# Optimize with sliding window
def nums_of_substring_three_char(s):
    """
    Count the number of substrings containing at least one occurrence of each of three specific characters.
    This function counts all substrings of the input string that contain at least one occurrence 
    of each of the first three characters of the alphabet ('a', 'b', and 'c').
    Args:
        s (str): The input string to analyze. Should contain lowercase alphabetic characters.
    Returns:
        int: The total count of substrings that contain at least one occurrence of 'a', 'b', and 'c'.
    Algorithm:
        - Maintains a list of last seen indices for characters 'a', 'b', and 'c'.
        - Iterates through the string, updating the last seen index for each character.
        - For each position where all three characters have been seen at least once,
          counts all valid substrings ending at the current position.
        - The count contribution is based on the minimum index among the three characters,
          which represents the earliest position in the current window.
    Time Complexity:
        O(n) where n is the length of the input string.
    Space Complexity:
        O(1) as only a fixed-size array of 3 elements is used.
    Example:
        >>> nums_of_substring_three_char("abacabad")
        4
    """

    last_seen = [-1, -1, -1]
    count = 0
    n = len(s)

    for i in range(n):
        # ord for ASCII '-' for the index 
        char_idx = ord(s[i]) - ord('a')

        last_seen[char_idx] = i

        if last_seen[0] != -1 and last_seen[1] != -1 and last_seen[2] != -1:
            count = count + (1 + min(last_seen[0], last_seen[1], last_seen[2]))

    return count

print("nums_of_substring_three_char", nums_of_substring_three_char(s))
