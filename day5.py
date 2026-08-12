#factorial
factorial = int(input("Enter the factorial number: "))
result = 1
for num in range(1, factorial + 1):
    result *= num
print("Factorial =", result)

#level EASY

#Q2. Factorial of 1

factorial = 1

for i in range(1, 2):
    factorial = factorial * i
print(factorial)

#Q5. Factorial from 1 to 10

result=1
for num in range(1,11):
    result= result*num
    print(f"{num}!={result}")

#🟡 Level 2 — Medium
#Q6. Calculate the sum of factorials from 1 to 5.
result = 1
total = 0

for num in range(1, 6):
    result = result * num
    total = total + result

print("Sum of factorials =", total)
#🟡 Q7 — Factorials of EVEN numbers
for num in range(1, 11):

    if num % 2 == 0:
        result = 1

        for i in range(1, num + 1):
            result = result * i

        print(f"{num}! = {result}")

