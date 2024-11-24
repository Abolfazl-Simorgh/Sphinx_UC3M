def add(a, b):
    """
    Add two numbers.

    Parameters
    ----------
    a : float
        The first number.
    b : float
        The second number.

    Returns
    -------
    float
        The sum of the two numbers.

    Examples
    --------
    >>> add(2, 3)
    5
    """
    return a + b


def subtract(a, b):
    """
    Subtract one number from another.

    Parameters
    ----------
    a : float
        The number to subtract from.
    b : float
        The number to subtract.

    Returns
    -------
    float
        The result of the subtraction.

    Examples
    --------
    >>> subtract(5, 3)
    2
    """
    return a - b


def multiply(a, b):
    """
    Multiply two numbers.

    Parameters
    ----------
    a : float
        The first number.
    b : float
        The second number.

    Returns
    -------
    float
        The product of the two numbers.

    Examples
    --------
    >>> multiply(4, 3)
    12
    """
    return a * b


def divide(a, b):
    """
    Divide one number by another.

    Parameters
    ----------
    a : float
        The numerator.
    b : float
        The denominator.

    Returns
    -------
    float
        The result of the division.

    Raises
    ------
    ZeroDivisionError
        If `b` is zero.

    Examples
    --------
    >>> divide(10, 2)
    5.0
    """
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a / b