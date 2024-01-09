# Hello World! 출력
print("Hello World!")

# 문장 출력
print("Day 1 - Python Print Function")
print("The function is declared like this:")

# 미션) 출력1
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('What to print')")

# 줄바꿈 처리
print("Hello world!\nHello world!\nHello world!")

# 공백 넣기
print("Hello " + "Angela")
print("Hello" + " Angela")
print("Hello" + " " + "Angela")

# 미션) 출력2
print("Day 1 - Python Print Function")
print('String Concatenation is done with the "+" sign.')
print("e.g" + ' print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

# 데이터 입력
print("Hello " + input("What is your name? "))

# 미션) 입력된 데이터 글자 수
print(len(input("What is your name? ")))

# 변수 사용
name = input("What is your name? ")
print(name)

# 변수 데이터 변경
name = "Jack"
print(name)

name = "Angela"
print(name)

# 변수 활용
name = input("What is your name?")
length = len(name)
print(length)

# 미션) 변수
a = input()
b = input()

print("a: " + b)
print("b: " + a)

# 프로젝트
print("Welcome to the Band Name Generator.")
print("What's name of the city you grew up in?")
city = input()
print("What's your pet's name?")
pet = input()
print("your band name could be" + " " + city + " " + pet)

# 강사 해답
print("Welcome to the Band Name Generator.")
city = input("What's name of the city you grew up in?\n")
pet = input("What's your pet's name?\n")
print("your band name could be" + " " + city + " " + pet)