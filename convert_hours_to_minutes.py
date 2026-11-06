def convert_hours_to_minutes(hours):
    """
    Convert hours to minutes.
    
    Args:
        hours (int or float): The number of hours to convert.
        
    Returns:
        int or float: The equivalent number of minutes.
    """
    return hours * 60

if __name__ == "__main__":
    # Example usage
    hours = 5
    minutes = convert_hours_to_minutes(hours)
    print(f"{hours} hours is equal to {minutes} minutes")