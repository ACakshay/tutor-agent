from tutor_agent.common_tools import evaluate_expression

import numpy as np


def solve_polynomial(coefficients):
    """
    This tool solves an nth-order single-variable polynomial equation numerically.

    Args:
        coefficients (list): Polynomial coefficients in descending order of powers.
                             E.g., [1, 0, -2, 1] corresponds to x^3 - 2x + 1 = 0

    Returns:
        numpy.ndarray: Array of roots (may include complex numbers)
    """

    # Use numpy.roots to compute all roots
    roots = np.roots(coefficients)

    return str(roots)


def get_tools():
    return [evaluate_expression]
