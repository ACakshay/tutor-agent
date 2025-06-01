from tutor_agent.common_tools import evaluate_expression


import pint
from pint import UnitRegistry


def convert_units_general(value: float, from_unit: str, to_unit: str):
    """
    A general-purpose unit conversion function covering a wide range of categories.

    Uses the 'pint' library for robust and accurate unit handling.

    Args:
        value (float or int): The numeric value to convert.
        from_unit (str): The unit of the input value (e.g., 'meters', 'km', 'joules', 'eV').
        to_unit (str): The desired unit for the output (e.g., 'feet', 'miles', 'kWh', 'celsius').

    Returns:
        float: The converted value in the target unit.

    Raises:
        ValueError: If units are unknown, incompatible, or conversion fails.
        TypeError: If value is not a number.
    """
    if not isinstance(value, (int, float)):
        raise TypeError("Value must be a number (int or float).")

    # Initialize the UnitRegistry from pint
    ureg = UnitRegistry()

    try:
        # Create quantities from the input value and units
        quantity = value * ureg(from_unit)

        # Convert to the target unit
        converted_quantity = quantity.to(to_unit)

        return str(converted_quantity.magnitude)
    except pint.errors.UndefinedUnitError as e:
        raise ValueError(
            f"Undefined unit error: {e}. Check if '{from_unit}' or '{to_unit}' is a valid unit."
        )
    except pint.errors.DimensionalityError as e:
        raise ValueError(
            f"Incompatible units: {e}. Cannot convert from '{from_unit}' to '{to_unit}'."
        )
    except Exception as e:
        # Catch any other unexpected errors from pint or general processing
        raise ValueError(f"An error occurred during conversion: {e}")


def get_tools():
    return [evaluate_expression, convert_units_general]
