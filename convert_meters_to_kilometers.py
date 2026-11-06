def convert_meters_to_kilometers(meters):
    """
    Convert a distance from meters to kilometers.

    Parameters
    ----------
    meters : float or int
        The distance in meters.

    Returns
    -------
    float
        The distance in kilometers.
    """
    try:
        return float(meters) / 1000.0
    except (TypeError, ValueError):
        raise ValueError("Input must be a numeric value representing meters.")


if __name__ == "__main__":
    try:
        user_input = input("Enter distance in meters: ").strip()
        meters = float(user_input)
        kilometers = convert_meters_to_kilometers(meters)
        print(f"{meters} meters is equal to {kilometers} kilometers")
    except Exception as e:
        print(f"Error: {e}")