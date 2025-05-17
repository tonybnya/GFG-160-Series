"""
Test 004. Rotate Array
"""

import pytest

from gfg_004_rotate_array import rotate_array_1, rotate_array_2


@pytest.mark.parametrize(
    "arr, d, expected",
    [
        # Basic cases
        ([1, 2, 3, 4, 5], 2, [3, 4, 5, 1, 2]),
        ([2, 4, 6, 8, 10, 12, 14, 16, 18, 20], 3, [8, 10, 12, 14, 16, 18, 20, 2, 4, 6]),
        # d > len(arr)
        ([7, 3, 9, 1], 9, [3, 9, 1, 7]),  # 9 % 4 = 1
        # d == 0 (no rotation)
        ([5, 6, 7], 0, [5, 6, 7]),
        # d == len(arr) (full rotation, should result in same array)
        ([10, 20, 30, 40], 4, [10, 20, 30, 40]),
        # Single element
        ([42], 1, [42]),
        # All elements the same
        ([9, 9, 9, 9], 2, [9, 9, 9, 9]),
        # Rotation by 1
        ([100, 200, 300], 1, [200, 300, 100]),
        # Rotation by len-1
        ([1, 2, 3, 4, 5], 4, [5, 1, 2, 3, 4]),
        # Large `d` with large array (edge case simulation)
        ([i for i in range(1, 11)], 13, [4, 5, 6, 7, 8, 9, 10, 1, 2, 3]),  # 13 % 10 = 3
    ],
)
def test_rotate_array_1(arr: list[int], d: int, expected: list[int]) -> None:
    """
    Test.
    """
    assert rotate_array_1(arr, d) == expected


@pytest.mark.parametrize(
    "arr, d, expected",
    [
        # Basic cases
        ([1, 2, 3, 4, 5], 2, [3, 4, 5, 1, 2]),
        ([2, 4, 6, 8, 10, 12, 14, 16, 18, 20], 3, [8, 10, 12, 14, 16, 18, 20, 2, 4, 6]),
        # d > len(arr)
        ([7, 3, 9, 1], 9, [3, 9, 1, 7]),  # 9 % 4 = 1
        # d == 0 (no rotation)
        ([5, 6, 7], 0, [5, 6, 7]),
        # d == len(arr) (full rotation, should result in same array)
        ([10, 20, 30, 40], 4, [10, 20, 30, 40]),
        # Single element
        ([42], 1, [42]),
        # All elements the same
        ([9, 9, 9, 9], 2, [9, 9, 9, 9]),
        # Rotation by 1
        ([100, 200, 300], 1, [200, 300, 100]),
        # Rotation by len-1
        ([1, 2, 3, 4, 5], 4, [5, 1, 2, 3, 4]),
        # Large `d` with large array (edge case simulation)
        ([i for i in range(1, 11)], 13, [4, 5, 6, 7, 8, 9, 10, 1, 2, 3]),  # 13 % 10 = 3
    ],
)
def test_rotate_array_2(arr: list[int], d: int, expected: list[int]) -> None:
    """
    Test.
    """
    assert rotate_array_2(arr, d) == expected
