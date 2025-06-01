from tutor_agent.common_tools import evaluate_expression

import numpy as np

import numpy as np


def solve_polynomial(coefficients: list[float]) -> str:
    """
    Solves an nth-order single-variable polynomial equation from list of coefficients.

    Args:
        coefficients (list): list of coefficients in descending order of powers.

    Returns:
        str: String representation of the polynomial roots
    """
    # Convert to floats for numpy
    coefficients = [float(c) for c in coefficients]

    # Compute roots
    roots = np.roots(coefficients)

    return str(roots)


def get_tools():
    return [solve_polynomial, evaluate_expression]
