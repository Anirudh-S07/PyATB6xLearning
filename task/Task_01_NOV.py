"""

1️⃣ Write a Function to Check Test Case Status

Problem:

Write a function check_status(status_code) that returns:

"PASS" if status_code = 200

"FAIL" if status_code = 400 or 500

"UNKNOWN" otherwise

Example Input & Output:

print(check_status(200))   # PASS

print(check_status(500))   # FAIL

print(check_status(302))   # UNKNOWN

"""


def check_status(status_code):
    if status_code == 200:
        return "Pass"
    elif status_code == 400 or status_code == 500:
        return "Fail"
    else:
        return "UNKNOWN"


input_status_code = int(input("Please input the status code"))

print(check_status(input_status_code))
