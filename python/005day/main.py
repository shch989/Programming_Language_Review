# # 반복문
# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#   print(fruit)
#   print(fruit + " Pie")
# print(fruits)

# # 미션) 평균 높이
# student_heights = input().split()

# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])

# total_height = sum(student_heights)
# number_of_students = len(student_heights)
# average_height = int(total_height / number_of_students)

# print(f"total height = {total_height}")
# print(f"number of students = {number_of_students}")
# print(f"average height = {average_height}")

# # 미션) 가장 큰 수
# student_scores = input().split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])

# highest_score = 0

# for score in student_scores:
#   if score > highest_score:
#     highest_score = score

# print(highest_score)

# # Range 함수
# for number in range(1, 11, 3):
#   print(number)

# total = 0 
# for number in range(1, 101):
#   total += number
# print(total)

# # 미션) 짝수 더하기
# target = int(input())

# even_sum = 0
# for number in range(2, target + 1, 2):
#   even_sum += number
# print(even_sum)

# # 미션) FizzBuzz
# target = 100
# for number in range(1, target + 1):
#   if number % 3 == 0 and number % 5 == 0:
#     print("FizzBuzz")
#   elif number % 3 == 0:
#     print("Fizz")
#   elif number % 5 == 0:
#     print("Buzz")
#   else:
#     print(number)

# 프로젝트
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

passwords = []

for n in range(nr_letters):
  passwords.append(letters[random.randint(0, len(letters) -1)])

for n in range(nr_numbers):
  passwords.append(numbers[random.randint(0, len(numbers) - 1)])

for n in range(nr_symbols):
  passwords.append(symbols[random.randint(0, len(symbols) - 1)])

random.shuffle(passwords)

your_password = ""

for password in passwords:
  your_password += password

print(f"Your password is: {your_password}")