"""
Test 011. Maximum Product Subarray
"""

import pytest

from gfg_011_maximum_product_subarray import max_product_1, max_product_2


@pytest.mark.parametrize(
    "arr, expected",
    [
        # Format: (arr, expected)

        # Test Case 1: From prompt
        ([-2, 6, -3, -10, 0, 2], 180),

        # Test Case 2: From prompt
        ([-1, -3, -10, 0, 6], 30),

        # Test Case 3: From prompt (all positive)
        ([2, 3, 4], 24),

        # Test Case 4: Contains zero separating max product subarrays
        ([1, 2, 0, -1, -3, -10], 30),

        # Test Case 5: All negative, even count
        ([-1, -2, -3, -4], 24),  # entire array

        # Test Case 6: All negative, odd count
        ([-1, -2, -3], 6),  # [-2, -3]

        # Test Case 7: Single element (positive)
        ([5], 5),

        # Test Case 8: Single element (negative)
        ([-5], -5),

        # Test Case 9: Multiple zeros
        ([0, -2, 0, -1, 0], 0),

        # Test Case 10: Mix of positive, negative and zeros
        ([1, -2, -3, 0, 7, -8, -2], 112),

        # Test Case 11: Ends with max product subarray
        ([0, 1, -2, -3, 4], 24),  # [-2, -3, 4]

        # Test Case 12: All zeros
        ([0, 0, 0], 0),
    ],
)
def test_max_product_1(arr: list[int], expected: int) -> None:
    """
    Test.
    """
    assert max_product_1(arr) == expected


@pytest.mark.parametrize(
    "arr, expected",
    [
        # Format: (arr, expected)

        # Test Case 1: From prompt
        ([-2, 6, -3, -10, 0, 2], 180),

        # Test Case 2: From prompt
        ([-1, -3, -10, 0, 6], 30),

        # Test Case 3: From prompt (all positive)
        ([2, 3, 4], 24),

        # Test Case 4: Contains zero separating max product subarrays
        ([1, 2, 0, -1, -3, -10], 30),

        # Test Case 5: All negative, even count
        ([-1, -2, -3, -4], 24),  # entire array

        # Test Case 6: All negative, odd count
        ([-1, -2, -3], 6),  # [-2, -3]

        # Test Case 7: Single element (positive)
        ([5], 5),

        # Test Case 8: Single element (negative)
        ([-5], -5),

        # Test Case 9: Multiple zeros
        ([0, -2, 0, -1, 0], 0),

        # Test Case 10: Mix of positive, negative and zeros
        ([1, -2, -3, 0, 7, -8, -2], 112),

        # Test Case 11: Ends with max product subarray
        ([0, 1, -2, -3, 4], 24),  # [-2, -3, 4]

        # Test Case 12: All zeros
        ([0, 0, 0], 0),
    ],
)
def test_max_product_2(arr: list[int], expected: int) -> None:
    """
    Test.
    """
    assert max_product_2(arr) == expected
