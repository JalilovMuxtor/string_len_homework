def main(s):
    """
    A string variable s is given. Return the "*" sign that is equal to the length of this variable.
    Args:
        s: string
    Returns:
        string
    """
    b=len(s)
    symbol='*'
    return symbol*b
print(main('codeschool'))