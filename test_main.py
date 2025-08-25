import pytest
from main import safe_divide, categorize_item

@pytest.mark.parametrize(
    "a,b,expected", [
        (6, 2, 3.0),        # normal division
        (5, 0, float('inf')), # division by zero
        (-10, -2, 5.0),     # negatives
        (0, 5, 0.0),        # zero numerator
    ]
)
def test_safe_divide(a, b, expected):
    assert safe_divide(a, b) == expected


@pytest.mark.parametrize(
    "item,expected", [
        ("apple", "fruit"),
        ("banana", "fruit"),
        ("carrot", "vegetable"),
        ("laptop", "other"),
    ]
)
def test_categorize_item(item, expected):
    assert categorize_item(item) == expected
