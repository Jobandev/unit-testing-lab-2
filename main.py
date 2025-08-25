def safe_divide(a: float, b: float) -> float:
    """
    Divides a by b, handling division by zero.
    Returns 'inf' if b == 0.
    """
    try:
        return a / b
    except ZeroDivisionError:
        return float('inf')


def categorize_item(name: str) -> str:
    """
    Categorize an item into groups:
    - "apple", "banana", "orange" → "fruit"
    - "carrot", "potato" → "vegetable"
    - otherwise → "other"
    """
    fruits = {"apple", "banana", "orange"}
    vegetables = {"carrot", "potato"}

    if name.lower() in fruits:
        return "fruit"
    elif name.lower() in vegetables:
        return "vegetable"
    else:
        return "other"
