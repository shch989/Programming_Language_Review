# 출력과 함수
def format_name(f_name, l_name):
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  return f"{formated_f_name} {formated_l_name}"

print(format_name("SEONG HYEON", "jo"))

# 다양한 리턴값
def format_name(f_name, l_name):
  if f_name == "" or l_name == "":
    return "You didin't provide valid inputs."
  else:
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

print(format_name(input("What is your first name? "), 
                  input("What is your last name? ")))

# 미션) 월별 일수
def ls_leep(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else: 
      return True
  else:
    return False

def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if month == 2 and ls_leep(year):
    return 29
  else:
    return month_days[month - 1]

year = int(input())
month = int(input())
days = days_in_month(year, month)
print(days)

# 독스트링
def format_name(f_name, l_name):
  """Take a first and last name and format it
  to return the title case version of the name."""
  if f_name == "" or l_name == "":
    return "You didin't provide valid inputs."
  else:
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

format_name()

# 프로젝트) 계산기 만들기
import os
from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)

  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  should_continue = True
 
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      os.system('cls')
      calculator()

calculator()