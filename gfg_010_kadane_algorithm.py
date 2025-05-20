"""
010. Kadane's Algorithm

Given an integer array arr[]. You need to find the maximum sum of a subarray.

Examples:

Input: arr[] = [2, 3, -8, 7, -1, 2, 3]
Output: 11
Explanation: The subarray {7, -1, 2, 3} has the largest sum 11.

Input: arr[] = [-2, -4]
Output: -2
Explanation: The subarray {-2} has the largest sum -2.

Input: arr[] = [5, 4, 1, 7, 8]
Output: 25
Explanation: The subarray {5, 4, 1, 7, 8} has the largest sum 25.

Constraints:
1 ≤ arr.size() ≤ 10^5
-109 ≤ arr[i] ≤ 10^4
"""


def max_subarray_sum_1(arr: list[int]) -> int:
    """
    Solution 1: Two Loops
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    n: int = len(arr)
    ans: int = arr[0]

    for i in range(n):
        s: int = 0
        for j in range(i, n):
            s += arr[j]
            ans = max(ans, s)

    return ans


def max_subarray_sum_2(arr: list[int]) -> int:
    """
    Solution 2: Dynamic Slinding Window
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    n: int = len(arr)
    ans: int = arr[0]
    max_ending: int = arr[0]

    for i in range(1, n):
        max_ending = max(max_ending + arr[i], arr[i])
        ans = max(ans, max_ending)

    return ans
