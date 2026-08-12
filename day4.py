# #for loop

# fruits = ["apple"]
# for fruit in range(5):
#     print(fruits[0])

# #using range
# for i in range(4): #range STOP
#     print (i)
# for i in range(2,6):#range START, STOP
#     print(i)
# for i in range(4,8,2):#range START, STOP, STEP
#     print(i)

# # Example of break
# for num in range(1, 10):
#     if num == 5:
#         break  # Stops completely when num hits 5
#     print(num)  

# # # Example of continue
# for num in range(1, 6):
#     if num == 3:
#         continue  # Skips 3 entirely
#     print(num) 

# # 🟢Level 1 — EASY

# #Print numbers 1 to 10
# for num in range (1,11):
#     print(num)

# #Print numbers 10 to 1
# for num in range(10,0,-1):
#     print (num)

# #Print even numbers from 1 to 20.
# for num in range(2,21,2):
#     print(num)

# # Print multiples of 5 from 5 to 50
# for num in range(5,51,5):
#     print(num)

# #Print the multiplication table of 5
# for num in range(1, 11):
#     print(5 * num)

# #🟡 Level 2 — MEDIUM

# #Print all numbers from 1 to 100 that are divisible by 3
# for i in range(3,101):
#     print(i)

# #Print numbers from 1 to 100 that are divisible by both 3 and 5.
# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print(i)

# #Find the sum of numbers from 1 to 100.
# #  Start with a total score of 0
# total_sum = 0

# # #  Loop through numbers from 1 to 100
# for i in range(1, 101):
#     total_sum = total_sum + i  # Add the current number to the total

# #  Print the final answer
# print("The sum is:", total_sum)

# #print the output like a tables

num=int(input("Enter the number:"))
if num in range(1,8):
    print(f"7 x {num}={7 * num}")