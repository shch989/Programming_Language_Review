# 모듈
import random

# 랜덤 숫자
random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.random()
print(random_float)

randomFloat = random.random() * 5
print(randomFloat)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")

# 미션) 동전 앞뒤
random_side = random.randint(0, 1)
if random_side == 0:
  print("Tails")
else:
  print("Heads")

# 배열
state_of_america = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado",
                    "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", 
                    "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", 
                    "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", 
                    "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", 
                    "New Hampshire", "New Jersey", "New Mexico", "New York", 
                    "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", 
                    "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", 
                    "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", 
                    "West Virginia", "Wisconsin", "Wyoming"]

state_of_america[1] = "Pencilvania"

state_of_america.append("Angelaland")

state_of_america.extend(["Angelaland", "Jack Bauer Land"])

print(state_of_america)

# 미션) 무작위 이름 출력
names_string = input()
names = names_string.split(", ")

num_items = len(names)

random_choice = random.randint(0, num_items -1)
print(names[random_choice])

# 중첩 리스트
fruits = ["Apple", "Banana", "Orange", "Grapes", "Strawberry", "Watermelon", "Pineapple"]
vegetables = ["Carrot", "Broccoli", "Tomato", "Spinach", "Cucumber"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)

# 미션) 보물지도
line1 = ["⬜️", "⬜️", "⬜️"]
line2 = ["⬜️", "⬜️", "⬜️"]
line3 = ["⬜️", "⬜️", "⬜️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input()

letter = position[0].lower()
abc = ["a", "b", "c"]
letter_index = abc.index(letter)
number_index = int(position[1]) - 1
map[number_index][letter_index] = 'X'

print(f"{line1}\n{line2}\n{line3}")

# 프로젝트
shapes = ['''
      _______
  ---'   ____)
        (_____)
        (_____)
        (____)
  ---.__(___)
  ''', '''
      _______
  ---'   ____)____
            ______)
            _______)
          _______)
  ---.__________)
  ''', '''
      _______
  ---'   ____)____
            ______)
        __________)
        (____)
  ---.__(___)
  '''
]

user_choice = int(input("What do you choice? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)

print(shapes[computer_choice])
print("Computer choice:")
print(shapes[user_choice])

if user_choice == computer_choice:
  print("You Draw")
if (user_choice == 0 & computer_choice == 1) or (user_choice == 1 & computer_choice == 2) or (user_choice == 2 & computer_choice == 0):
  print("You Lose")
if (user_choice == 0 & computer_choice == 2) or (user_choice == 1 & computer_choice == 0) or (user_choice == 2 & computer_choice == 1):
  print("You Win")