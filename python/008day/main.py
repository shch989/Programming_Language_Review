# 함수 실행
def greet():
  print(f"Hello")
  print(f"how do you do?")
  print("Isn't the weather nice today?")

greet()

# 함수와 입력 값
def greet_with_name(name):
  print(f"Hello {name}")
  print(f"How do you do {name}?")

greet_with_name("Seong Hyeon")

# 위치 인자
def greet_with(name, location):
  print(f"Hello {name}")
  print(f"What is it like in {location}")

greet_with("Seong Hyeon", "Nowhere")

# 키워드 인자
def greet_with(name="Seong Hyeon", location="Nowhere"):
  print(f"Hello {name}")
  print(f"What is it like in {location}")

greet_with()

# 미션) 페인트 면적 계산기
import math

test_h = int(input())
test_w = int(input())
coverage = 5
def paint_calc(height=test_h, width=test_w, cover=coverage):
  num_cans = (height * width) / cover
  round_up_cans = math.ceil(num_cans)
  print(f"You'll seed {round_up_cans} cans of paint.")

paint_calc()

# 미션) 소수 확인기
def prime_checker(number):
  is_prime = 0
  for i in range(1, number + 1):
    if number % i == 0:
      is_prime += 1
  if is_prime == 2:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")

n = int(input())
prime_checker(number=n)

# 또 다른 방식
def prime_checker(number):
  is_prime = True
  for i in range(2, number):
    if number % i == 0:
      is_prime = False
  if is_prime:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")

n = int(input())
prime_checker(number=n)

# 카이사르 암호 - 암호화 및 복호화
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    new_letter = alphabet[new_position]
    cipher_text += new_letter
  print(f"The encoded text is {cipher_text}")

def decrypt(cipher_text, shift_amount):
  plain_text = ""
  for letter in cipher_text:
    position = alphabet.index(letter)
    new_position = position - shift_amount
    new_letter = alphabet[new_position]
    plain_text += new_letter
  print(f"The decoded text is {plain_text}")

if direction.lower() == "encode":
  encrypt(plain_text=text, shift_amount=shift)
elif direction.lower() == "decode":
  decrypt(cipher_text=text, shift_amount=shift)
else:
  print("Error")

# 코드 개선
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
      shift_amount *= -1
  for letter in start_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    end_text += alphabet[new_position]
  print(f"Here's the {direction}d result: {end_text}")

caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

# 유저관점 개선
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"Here's the {cipher_direction}d result: {end_text}")

from art import logo
print(logo)

should_end = False
while not should_end:

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_end = True
    print("Goodbye")
    