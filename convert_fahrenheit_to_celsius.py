def convert_fahrenheit_to_celsius(fahrenheit):
    """
    Convert a temperature from Fahrenheit to Celsius.
    
    Args:
        fahrenheit (float): Temperature in Fahrenheit.
        
    Returns:
        float: Temperature in Celsius.
    """
    return (fahrenheit - 32) * 5 / 9

if __name__ == "__main__":
    f_temp = float(input("Enter temperature in Fahrenheit: "))
    c_temp = convert_fahrenheit_to_celsius(f_temp)
    print(f"{f_temp}°F is equal to {c_temp:.2f}°C")