#String and Integer
age = 19
name = "Gianna"
print("Hello, World!", "My name is", name, "and my age is", age)


#Float (Decimal)
price = 9.99
print("$", price)


#Boolean (t/f)
is_logged_in = True
is_admin = False

#Arithmetic Operations (+ - * /)
print(5 + 8)
print(10 - 4)
print(6 * 7)
print(12 / 2)

#Modulous % (Remainder)
print(580 % 2) #EVEN
print(559 % 2) #ODD

#Comparison Operators (== != > < >= <=)
print(5 == 5) #CHECKS IF EQUAL
print(4 != 5) #CHECKS IF NOT EQUAL
print(8 > 10) #CHECKS IF GREATER/LESS
print(10 <= 8) #CHECKS IF GREATER/LESS OR EQUAL

#User Input
name = input("Enter your name: ")
print("Hello,", name)
age = input("Enter your age: ")

#Ways to connect a string with a integer in between!!!
print("You are " + age + " years old.")
print(f"You are {age} years old.")

#Conditional Statements
age = 20
if age >= 18:
    print("You are an adult!")
else:
    print("You are a child!")

#Multiple Conditions (ORDER MATTERS!!!)
score = 95
if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
else:
    print("You need to study!")

#Logical Operators
age = 20
has_id = True
if age >= 18 and has_id:
    print("You can enter")
else:
    print("You can not enter")

day = "Saturday"
if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")








#SMALL BUILDS

#Mini Calculator (CASTING/CONVERTING NUM)
num1 = int(input("Number1: "))
num2 = int(input("Number2: "))
print(f"The result is {num1 + num2}!")

#Score Checker
score = int(input("Enter your exam score: "))
if score >= 90:
    print("Excellent!")
elif score >= 80:
    print("Good Job!")
elif score >= 70:
    print("Good Effort!")
else:
    print("Study More!")