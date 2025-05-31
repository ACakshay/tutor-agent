import periodictable


def get_atomic_properties(symbol: str) -> dict:
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
            "mass_number": element.mass_number,
        }
    except KeyError:
        raise ValueError(f"Element symbol '{symbol}' not found.")


def get_tools():
    return []
