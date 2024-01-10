# 조건문 사용
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  print("You can ride the rollercoaster!")
else:
  print("Sorry, you have to grow taller before you can ride.")

# 미션) 홀수 짝수
number = int(input())

if number % 2 == 1:
  print("This is an odd number.")
else:
  print("This is an even number.")

# 중첩 if문과 elif
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    print("Please pay $5.")
  elif age <= 18:
    print("Please pay $7.")
  else:
    print("Please pay $12.")
else:
  print("Sorry, you have to grow taller before you can ride.")

# 미션) BMI 2.0
height = float(input())
weight = int(input())

bmi = weight / height ** 2

if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")

# 미션) 윤년
year = int(input())

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year")
    else:
      print("Not Leap year")
  else: 
    print("Leap year")
else:
  print("Not leap year")

# 다중 연속 if문
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Please pay $5.")
  elif age <= 18:
    bill = 7
    print("Please pay $7.")
  else:
    bill = 12
    print("Please pay $12.")

  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo == "Y":
    bill += 3

  print(f"Your final bill is ${bill}")

else:
  print("Sorry, you have to grow taller before you can ride.")

# 미션) 피자 주문
size = input()
add_pepperoni = input()
extra_cheese = input()

bill = 0

if size == "S":
  bill += 15
  if add_pepperoni == "Y":
    bill += 2
elif size == "M":
  bill += 20
  if add_pepperoni == "Y":
    bill += 3
else:
  bill += 25
  if add_pepperoni == "Y":
    bill += 3

if extra_cheese == "Y":
  bill += 1

print("Thank you for choosing Python Pizza Deliveries!")
print(f"Your final bill if: ${bill}.")

# 논리 연산자
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Please pay $5.")
  elif age <= 18:
    bill = 7
    print("Please pay $7.")
  elif age >= 45 and age <= 55:
    print("Everything is going to be ok, Have a free ride on us!")
  else:
    bill = 12
    print("Please pay $12.")

  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo == "Y":
    bill += 3

  print(f"Your final bill is ${bill}")

else:
  print("Sorry, you have to grow taller before you can ride.")

# 미션) 사랑 계산기
name1 = input()
name2 = input()

name = name1 + name2
name_as_lower = name.lower()

t = name_as_lower.count("t")
r = name_as_lower.count("r")
u = name_as_lower.count("u")
e = name_as_lower.count("e")
true_total = t + r + u + e

l = name_as_lower.count("l")
o = name_as_lower.count("o")
v = name_as_lower.count("v")
e = name_as_lower.count("e")
love_total = l + o + v + e

score = str(true_total) + str(love_total)
score_as_int = int(score)

print("The Love Calculator is calculating your score...")

if score_as_int < 10 or score_as_int > 90:
  print(f"Your score is {score_as_int}, you go together like coke and mentos.")
elif score_as_int > 40 and score_as_int < 50:
  print(f"Your score is {score_as_int}, you are alright together.")
else:
  print(f"Your score is {score_as_int}")

# 프로젝트
print("Welcome to Tresure Island.")
print("Your mission is to find the treasure.")
choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or right\n').lower()
if choice1 == "right":
  print("You enter a room of beasts. Game Over.")
else:
  choice2 = input('You com to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
  if choice2 == "swim":
    print("You enter a room of beasts. Game Over.")
  else:
    choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n").lower()
    if choice3 == "red" or choice3 == "blue":
      print("You enter a room of beasts. Game Over.")
    else:
      print("You Win!")