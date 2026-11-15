
name = "matt anita"
nim = "2611538001"
username = "matt001"

intake_year = "20"  + nim[:2]

print("+" + "-" * 28 + "+")
print("|" + "STUDENT CARD".center(28) + "|")
print("+" + "-" * 28 + "+")

print(f"| {'Name':<10}: {name.title():<14} |")
print(f"| {'Name':<10}: {nim:<14} |")
print(f"| {'Username':<10}: {username:<14} |")
print(f" | {'Intake Year':<10}: {intake_year:<14} |")

print("+" + "-" * 28 + "+")