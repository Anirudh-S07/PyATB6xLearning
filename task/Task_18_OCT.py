"""
Q1 :
Given a number you need to calculate the factorial of that number
n = 5
Fact = 5×4×3*2*1 = 120
Fact = 0 → 1,
"""

number = int(input("please enter the number:"))
fact = 1
if number < 0:
    print("Factorial is defined only for numbers greater than or equal to zero")
else:
    for i in range(1, number+1):
        fact *= i
    print(f"The factorial of {number} is {fact}")

"""
Q-2 An API sometimes fails due to network delays.

Write a program to retry the API call 3 times until the response code becomes 200.

If it still fails after 3 tries, print a failure message.

Hint: Use a while loop with a counter.
Hint: Use a while loop with a counter.

Expected Output Example:

Attempt 1: Response 500

Attempt 2: Response 200

✅ Test Passed

"""
i = 0
while i < 3:
    response_code = int(input("Please enter the response in numbers: "))
    if response_code == 200:
        print("✅ Test Passed")
        break
    else:
        print("❌ Test Failed")
    i += 1

"""
Simulate a page loading check using a while loop.
If page_loaded becomes True within 5 seconds, print success; else timeout.

Hint: Use a counter (like wait_time) and break condition.

"""

wait_time = 0
page_loaded = False
while wait_time < 5:
    page_loaded_time = (input("Please enter if page has loaded in True/False: "))
    if page_loaded_time == "True":
        print("✅ Success Page has Loaded")
        page_loaded = True
        break
    else:
        print("⚠️ Waiting for the page to load")
    wait_time += 1
if not page_loaded:
    print("❌ Failed Page did not load")


