#elseif

# mark=int(input("Enter your mark:"))
# if mark < 0 or mark > 100:
#     print("Invalid mark. Please enter a mark between 0 and 100.")
# elif mark>=95:
#     print("Exellent")
# elif mark>=80:
#     print("Verry Good")
# elif mark>=70:
#     print("Good")
# elif mark>=50:
#     print("Need to improve")
# else:
#     print("Fail")

#nested if
#check whether the num is positve or negative
# num=int(input("Enter the Number:"))
# if num>0:
#     print("possitve")
# else:
#     print("Negative")

#Build a simulated login system that checks three separate layers of validation: a username, a password, and an account status
# username = "admin"
# password = "Secret123"
# is_active = True

# # Your solution should look like this:
# if username == "admin":
#     if password == "Secret123":
#         if is_active:
#             print("Welcome back, Admin!")
#         else:
#             print("Access Denied: Account Deactivated")
#     else:
#         print("Access Denied: Incorrect Password")
# else:
#     print("Access Denied: Unknown User")


# Scenario:
# Design the backend logic for an ATM machine processing a withdrawal transaction.
balance = 500
daily_limit = 300
amount = 120

if amount % 10 == 0:
    if amount <= balance:
        if amount <= daily_limit:
            balance -= amount
            print(f"Withdrawal successful. Remaining balance: ${balance}")
        else:
            print("Error: Exceeds daily withdrawal limit")
    else:
        print("Error: Insufficient funds")
else:
    print("Error: Please request a multiple of $10")


