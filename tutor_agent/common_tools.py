import math
import numexpr
import scipy.constants as sc_constants


class constants:

    @classmethod
    def __getitem__(self, key):
        if hasattr(sc_constants, key):
            return getattr(sc_constants, key)
        else:
            raise ValueError(f"scipy.constants module has no constant named '{key}'")


def evaluate_expression(expression: str):
    """
    use this tool to evaluates a mathematical expression using python numexpr.
    Only provide valid mathematical expressions.
    For constants, it uses scipy.constants so you can use constants like 'pi', 'e', etc. in expression.
    to just get the value of a constant, use the name of the constant directly.

    Args:
        expression (str): The mathematical expression to evaluate.

    Returns:
        The result of the evaluated expression.
    Example:
        "37593 * 67" for "37593 times 67"
        "37593**(1/5)" for "37593^(1/5)"
        "pi * 2" for "pi times 2"
        "h" for "Planck's constant"
    Raises:
        ValueError: If the expression is not a string or contains invalid characters.
    """
    # Ensure the expression is a string and strip any leading/trailing whitespace
    if not isinstance(expression, str):
        raise ValueError("Expression must be a string.")

    expression = expression.strip()

    # Evaluate the expression using numexpr with restricted globals and custom constants
    try:
        ans = numexpr.evaluate(
            expression.strip(),
            global_dict={},  # restrict access to globals
            local_dict=constants(),  # add common mathematical constants
        )
        return str(ans)
    except Exception as e:
        return f"Error evaluating expression: {repr(e)}"
