"""
check_voting_eligibility.py

Provides a simple function to determine if a person is eligible to vote
based on their age. The function follows the same style as other
`check_*` utilities in the repository, returning a human‑readable
string rather than a boolean.

Author: Senior Software Engineer
"""

def check_voting_eligibility(age: int) -> str:
    """
    Determine voting eligibility.

    Parameters
    ----------
    age : int
        The age of the person to check.

    Returns
    -------
    str
        "Eligible to vote" if age is 18 or older,
        otherwise "Not eligible to vote".

    Examples
    --------
    >>> check_voting_eligibility(20)
    'Eligible to vote'
    >>> check_voting_eligibility(16)
    'Not eligible to vote'
    """
    if age >= 18:
        return "Eligible to vote"
    return "Not eligible to vote"