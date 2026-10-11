def check_pass_or_fail(marks):
    if marks >= 40:
        return "Pass"
    else:
        return "Fail"

if __name__ == "__main__":
    marks = float(input("Enter marks: "))
    result = check_pass_or_fail(marks)
    print(result)