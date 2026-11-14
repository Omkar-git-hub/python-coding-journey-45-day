def check_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def check_temperature(temp):
    if temp < 0:
        return "Freezing"
    elif temp < 20:
        return "Cold"
    elif temp < 30:
        return "Moderate"
    elif temp < 40:
        return "Hot"
    else:
        return "Very Hot"

def check_number_range(num):
    if num < 0:
        return "Negative"
    elif num == 0:
        return "Zero"
    elif num < 10:
        return "Small Positive"
    elif num < 100:
        return "Medium Positive"
    else:
        return "Large Positive"

if __name__ == "__main__":
    print(check_grade(85))
    print(check_temperature(25))
    print(check_number_range(50))