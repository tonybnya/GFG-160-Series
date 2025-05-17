"""
Test 004. Rotate Array
"""

import pytest

from gfg_005_next_permutation import next_permutation_1, next_permutation_2


@pytest.mark.parametrize(
    "arr, expected",
    [
        # Already highest permutation → should return lowest
        ([3, 2, 1], [1, 2, 3]),
        # Middle of the permutation list
        ([2, 4, 1, 7, 5, 0], [2, 4, 5, 0, 1, 7]),
        # Single swap needed at the end
        ([1, 2, 3], [1, 3, 2]),
        # Needs partial reverse at the end
        ([1, 3, 2], [2, 1, 3]),
        # Requires scanning from right to find pivot
        ([3, 4, 2, 5, 1], [3, 4, 5, 1, 2]),
        # Single element → no change
        ([5], [5]),
        # Two elements - already highest
        ([2, 1], [1, 2]),
        # Already lowest permutation
        ([1, 1, 5], [1, 5, 1]),
        # All elements are same
        ([7, 7, 7], [7, 7, 7]),
        # Large ascending prefix with descending suffix
        ([1, 2, 3, 6, 5, 4], [1, 2, 4, 3, 5, 6]),
    ],
)
def test_next_permutation_1(arr: list[int], expected: list[int]) -> None:
    """
    Test.
    """
    assert next_permutation_1(arr) == expected


@pytest.mark.parametrize(
    "arr, expected",
    [
        # Already highest permutation → should return lowest
        ([3, 2, 1], [1, 2, 3]),
        # Middle of the permutation list
        ([2, 4, 1, 7, 5, 0], [2, 4, 5, 0, 1, 7]),
        # Single swap needed at the end
        ([1, 2, 3], [1, 3, 2]),
        # Needs partial reverse at the end
        ([1, 3, 2], [2, 1, 3]),
        # Requires scanning from right to find pivot
        ([3, 4, 2, 5, 1], [3, 4, 5, 1, 2]),
        # Single element → no change
        ([5], [5]),
        # Two elements - already highest
        ([2, 1], [1, 2]),
        # Already lowest permutation
        ([1, 1, 5], [1, 5, 1]),
        # All elements are same
        ([7, 7, 7], [7, 7, 7]),
        # Large ascending prefix with descending suffix
        ([1, 2, 3, 6, 5, 4], [1, 2, 4, 3, 5, 6]),
    ],
)
def test_next_permutation_2(arr: list[int], expected: list[int]) -> None:
    """
    Test.
    """
    assert next_permutation_2(arr) == expected
