# Package considered BULKY if volume >= 1,000,000 cm³
BULKY_VOLUME_CM3 = 10 ** 6
# Or if one of the dimensions is >= 150 cm
BULKY_DIMENSION_CM = 150
# Packages are HEAVY when mass >= 20 kg
HEAVY_MASS_KG = 20

def sort(width, height, length, mass) -> str:
    """Classifies a package as STANDARD, SPECIAL, or REJECTED based on its dimensions and mass.

    Args:
        width: Width of the package in centimeters (cm). Can be int, float, or numeric string.
        height: Height of the package in centimeters (cm). Can be int, float, or numeric string.
        length: Length of the package in centimeters (cm). Can be int, float, or numeric string.
        mass: Mass of the package in kilograms (kg). Can be int, float, or numeric string.

    Returns:
        str: 'STANDARD' (not bulky nor heavy), 'SPECIAL' (bulky or heavy), or 'REJECTED' (bulky and heavy).

    Raises:
        TypeError: If any input cannot be converted to a number.
        ValueError: If any dimension or mass is not positive or is not finite.
    """
    # Input validation
    params = {"width": width, "height": height, "length": length, "mass": mass}
    converted = {}
    for name, value in params.items():
        # Handle int, float, or numeric string
        if isinstance(value, (int, float)):
            converted[name] = float(value)
        elif isinstance(value, str):
            try:
                converted[name] = float(value)
            except ValueError:
                raise TypeError(f"{name} must be a number (int, float, or numeric string)")
        else:
            raise TypeError(f"{name} must be a number (int, float, or numeric string)")

        # Check for positive and finite values
        if converted[name] <= 0 or converted[name] in (float('inf'), float('-inf')) or converted[name] != converted[name]:
            raise ValueError(f"{name} must be a positive, finite number")

    width, height, length, mass = converted["width"], converted["height"], converted["length"], converted["mass"]

    volume = width * height * length
    is_bulky = check_if_bulky(volume, width, height, length)
    is_heavy = check_if_heavy(mass)

    if is_bulky and is_heavy:
        return "REJECTED"
    if is_bulky or is_heavy:
        return "SPECIAL"
    return "STANDARD"

def check_if_bulky(volume: float, width: float, height: float, length: float) -> bool:
    """Checks if a package is bulky based on volume or dimension thresholds.

    Args:
        volume: Volume of the package in cubic centimeters (cm³).
        width: Width of the package in centimeters (cm).
        height: Height of the package in centimeters (cm).
        length: Length of the package in centimeters (cm).

    Returns:
        bool: True if the package is bulky, False otherwise.
    """
    return volume >= BULKY_VOLUME_CM3 or any(dim >= BULKY_DIMENSION_CM for dim in [width, height, length])

def check_if_heavy(mass: float) -> bool:
    """Checks if a package is heavy based on mass threshold.

    Args:
        mass: Mass of the package in kilograms (kg).

    Returns:
        bool: True if the package is heavy, False otherwise.
    """
    return mass >= HEAVY_MASS_KG