# String 5번째 문자 출력
print("Hello"[4])

# String 병합
print("123" + "456")

# Number 합
print(123 + 456)

# Number 자릿수 표기
print(123_456_789)

# Float
print(3.14159)

# Boolean
print(True)
print(False)

# 데이터 타입 확인
num_char = len(input("What is your name?"))
print(type(num_char))

# 데이터 타입 변경
num_char = len(input("What is your name?"))
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")

# 타입 변경 활용
a = float(123)
print(type(a))
print(70 + float("100.5"))
print(str(70) + str(100))

# 미션) 입력받은 데이터의 합
two_digit_number = input()

first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

two_digit_number = first_digit + second_digit

print(two_digit_number)

# Number 연산 순서
print(3 * (3 + 3) / 3 - 3)

# 미션) BMI 계산기
height = input()
weight = input()

weight_as_int = int(weight)
height_as_float = float(height)

bmi = weight_as_int / height_as_float ** 2

bmi_as_int = int(bmi)
print(bmi_as_int)

# Number 반올림
print(round(8 / 3, 2))

# 소숫점 버림
print(8 / 3)
print(type(8 / 3))
print(8 // 3)
print(type(8 // 3))

# 변수 연산
result = 10
result += 2
print(result)

# String 변수 기입
score = 0
height = 1.8
isWinning = True

print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")

# 미션) 삶을 주로 표현
age = input()

years = 90 - int(age)
weeks = years * 52

print(f"You have {weeks} weeks left.")

# 프로젝트
print("Welcome to the tip calculator.")
total = input("What was the total bill? $")
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

total_as_float = float(total)
tip_as_int = int(tip)
people_as_int = int(people)

tip_total = total_as_float * (tip_as_int / 100)
pay = (total_as_float + tip_total) / people_as_int
pay_round = round(pay, 2)

print(f"Each person should pay: ${pay_round}")

# 강사 해답
print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")