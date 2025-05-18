"""
Test 007. Stock Buy and Sell – Multiple Transaction Allowed
"""

import pytest

from gfg_007_max_profit_multiple_allowed import max_profit


@pytest.mark.parametrize(
    "prices, expected",
    [
        # Format: (Input, Expected Output)
        # Test Case 1: Example from prompt
        ([100, 180, 260, 310, 40, 535, 695], 865),
        # Test Case 2: Flat prices (no profit)
        ([100, 100, 100, 100], 0),
        # Test Case 3: Strictly decreasing prices
        ([5, 4, 3, 2, 1], 0),
        # Test Case 4: Always increasing
        ([1, 2, 3, 4, 5], 4),
        # Test Case 5: Small valley
        ([4, 2, 2, 2, 4], 2),
        # Test Case 6: No movement
        ([3, 3, 3, 3], 0),
        # Test Case 7: Complex pattern
        ([7, 1, 5, 3, 6, 4], 7),
        # Test Case 8: Large spikes
        ([1, 1000, 1, 1000], 1998),
        # Test Case 9: Single day
        ([10], 0),
        # Test Case 10: Two days with profit
        ([1, 5], 4),
        # Test Case 11: Zigzag ups and downs
        ([2, 4, 1, 7], 8),  # buy at 2 sell at 4 (2), buy at 1 sell at 7 (6)
    ],
)
def test_max_profit(prices: list[int], expected: int) -> None:
    """
    Test.
    """
    assert max_profit(prices) == expected
