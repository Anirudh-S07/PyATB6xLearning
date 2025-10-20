"""
Q1  - You receive an API response code from your test script.
Write an if-else block to check whether the response is successful (status code 200) or not.

I/P response = 404 , O/P ❌ Failed API Request
I/P response = 200 , O/P ✅ Passed API Request
"""

api_input = int(input("please enter the response code :"))

if api_input == 200:
    print(f"I/P response = {api_input} , O/P ✅ Passed API Request")
else:
    print(f"I/P response = {api_input} , O/P ❌ Failed API Request")

"""
Q2 - In automation, you often compare expected and actual outputs.
Write code to check if a test case passed or failed.

expected_title = "Dashboard"
actual_title = "Dashboard "

✅ Test Passed – Title matches


True - why >  Strip and convert them into the lowercase = both of them are equal.
"""
expected_title = "Dashboard"
actual_title = input(" Please enter the actual title :\n")

if expected_title.strip().lower() == actual_title.lower().strip():
    print(f"{expected_title.strip().lower()} is the same as {actual_title.lower().strip()} "
          f"✅ Test Passed – Title matches")
else:
    print(
        f"{expected_title.strip().lower()} is not the same as {actual_title.lower().strip()} "
        f"❌ Test Failed – Title Does not match")

# alternate with ternary operator
# cause string cannot be mutated ie changed and called again with the same name
modified_expected = expected_title.strip().lower()
modified_actual = actual_title.lower().strip()
print(f"{modified_expected} is the same as {modified_actual} "
      f"✅ Test Passed – Title matches" if modified_expected == modified_actual else f"{modified_expected} is not "
      f"the same as {modified_actual}❌ Test Failed – Title Does not match")

"""
Q-3 You want to check whether a web page loads within 3 seconds (performance test condition).

load_time = 4.2
⚠️ Page load too slow: 4.2 seconds

"""

load_time = float(input("PLease enter the load time : \n"))

print(f"⚠️ Page load too slow: {load_time} seconds" if load_time > 3.0 else f"✅ Page is fine: {load_time} seconds")

# Alternate If Else Block

if load_time > 3.0:
    print(f"⚠️ Page load too slow: {load_time} seconds")
else:
    print(f"✅ Page is fine: {load_time} seconds")


"""
Q4 
Check if the user can log in based on correct username and password.

I/p

username = "admin"
password = "1234"
"""
username = input("Please enter the user name :").strip().lower()
password = input("Please enter the password :")

if username == "admin" and password == "1234":
    print(f"{username} and password are correct ✅ Login Successful")
else:
    print(f"{username} and password are not correct ❌ Login Un Successful")



