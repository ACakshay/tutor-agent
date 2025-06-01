import periodictable

from tutor_agent.common_tools import search_internet


def get_atomic_properties(symbol: str) -> dict:
    """
    This tool retrieve atomic properties of an element from it's chemical symbol.
    Args:
        symbol (str): The chemical symbol of the element (e.g., 'H', 'O', 'Na').

    Returns:

        dict: A dictionary containing the element's symbol, atomic number, and atomic mass.
    Raises:
        ValueError: If the symbol is not found in the periodic table."""

    try:
        # Normalize symbol to proper capitalization
        symbol = symbol.capitalize()
        # Retrieve the element object
        element = periodictable.elements.symbol(symbol)
        # Return the properties as a dictionary
        return {
            "symbol": element.symbol,
            "atomic_number": element.number,
            "atomic_mass": element.mass,
        }
    except KeyError:
        raise ValueError(f"Element symbol '{symbol}' not found.")


def get_tools():
    return [search_internet, get_atomic_properties]
