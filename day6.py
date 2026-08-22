#while loop

counter = 1

while counter <= 3:
    print(f"Count is: {counter}")
    counter += 1  # Updates the condition variable

print("Loop finished!")

#Write a program that starts at 5 and counts down to 1. Once it hits 0, it should print "Liftoff!"
counter = 5

while counter > 0:
    print(counter)
    counter -= 1  # Subtract 1 each time
print("Liftoff!")
#Create a program that adds numbers together from 1 up to 5 and prints the final total at the end.
# 1. Setup our starting variables
counter = 1
total = 0

# 2. Loop runs as long as counter is 5 or less
while counter <= 5:
    total += counter    # Add the current number to our total piggy bank
    counter += 1        # Move to the next number

# 3. Print the final result after the loop finishes completely
print(f"The total sum is: {total}")

#Question 3: Even Numbers Only (2 to 10)
# 1. Start directly at the first even number
counter = 2

# 2. Loop until we reach 10
while counter <= 10:
    print(counter)
    counter += 2  # Jump by 2 to hit the next even number
#Question 4: Guess the Magic Word

magic_word = "python"
guess = ""  # Start empty so it doesn't match "python" initially

# The loop keeps running WHILE the guess is NOT equal to "python"
while guess != magic_word:
    guess = input("Guess the magic word: ")

print("You got it!")


#function

def hello(): #create the function name
    print("Hii python")
hello() #calling function
hello()
hello()

#without function
result1=4*4
print(result1)
result2=5*5
print(result2)
result3=6*6
print(result3)

#with function
def square(num):
    return num*num
print(square(4))
print(square(5))
print(square(6))

#return value
def get_greeting():
  return "Hello from a function"

message = get_greeting()
print(message)

#fuction with argument
def greet(name):
    print("hello", name)
greet("priya")
greet("laya")

#add function
def add(a,b):
    print("Sum=",(a+b))
add(10,20)

#multiply
def multiply(a,b):
    print(a*b)
multiply(5,4)

#level 3 argument + return statement
def add(a,b):
    return a+b
result=add(10,20)
print (result)
