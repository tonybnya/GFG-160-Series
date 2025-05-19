"""
Test 008. Stock Buy and Sell – Max one Transaction Allowed
"""

import pytest

from gfg_008_max_profit_max_one_allowed import maximum_profit_1, maximum_profit_2


@pytest.mark.parametrize(
    "prices, expected",
    [
        # Format: (Input, Expected Output)
        # Test Case 1: Example from prompt
        ([7, 10, 1, 3, 6, 9, 2], 8),
        # Test Case 2: Decreasing prices — no profit
        ([7, 6, 4, 3, 1], 0),
        # Test Case 3: Increasing prices — max profit is last - first
        ([1, 3, 6, 9, 11], 10),
        # Test Case 4: Flat prices — no profit
        ([2, 2, 2, 2, 2], 0),
        # Test Case 5: Buy low (1), sell high (20)
        ([10, 8, 6, 4, 2, 1, 20], 19),
        # Test Case 6: Single day — cannot sell
        ([5], 0),
        # Test Case 7: Two days with profit
        ([1, 5], 4),
        # Test Case 8: Two days no profit
        ([5, 1], 0),
        # Test Case 9: Complex pattern
        ([3, 2, 6, 1, 3], 4),  # buy at 1, sell at 3
        # Test Case 10: Early peak, later dip
        ([9, 7, 4, 1, 2, 10], 9),  # buy at 1, sell at 10
        # Test Case 11: Multiple small gains, but only one transaction allowed
        ([1, 2, 1, 2, 1, 2], 1),
        # Test Case 12: Peak in the middle
        ([2, 4, 1, 7], 6),  # buy at 1, sell at 7
        # Test Case 13: Profit possible at end
        ([8, 6, 5, 4, 10], 6),  # buy at 4, sell at 10
    ],
)
def test_maximum_profit_1(prices: list[int], expected: int) -> None:
    """
    Test.
    """
    assert maximum_profit_1(prices) == expected


@pytest.mark.parametrize(
    "prices, expected",
    [
        # Format: (Input, Expected Output)
        # Test Case 1: Example from prompt
        ([7, 10, 1, 3, 6, 9, 2], 8),
        # Test Case 2: Decreasing prices — no profit
        ([7, 6, 4, 3, 1], 0),
        # Test Case 3: Increasing prices — max profit is last - first
        ([1, 3, 6, 9, 11], 10),
        # Test Case 4: Flat prices — no profit
        ([2, 2, 2, 2, 2], 0),
        # Test Case 5: Buy low (1), sell high (20)
        ([10, 8, 6, 4, 2, 1, 20], 19),
        # Test Case 6: Single day — cannot sell
        ([5], 0),
        # Test Case 7: Two days with profit
        ([1, 5], 4),
        # Test Case 8: Two days no profit
        ([5, 1], 0),
        # Test Case 9: Complex pattern
        ([3, 2, 6, 1, 3], 4),  # buy at 1, sell at 3
        # Test Case 10: Early peak, later dip
        ([9, 7, 4, 1, 2, 10], 9),  # buy at 1, sell at 10
        # Test Case 11: Multiple small gains, but only one transaction allowed
        ([1, 2, 1, 2, 1, 2], 1),
        # Test Case 12: Peak in the middle
        ([2, 4, 1, 7], 6),  # buy at 1, sell at 7
        # Test Case 13: Profit possible at end
        ([8, 6, 5, 4, 10], 6),  # buy at 4, sell at 10
    ],
)
def test_maximum_profit_2(prices: list[int], expected: int) -> None:
    """
    Test.
    """
    assert maximum_profit_2(prices) == expected
