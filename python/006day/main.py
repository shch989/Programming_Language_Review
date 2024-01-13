# 기본 함수
print("Hello")
num_char = len("Hello")
print(num_char)

# 함수 정의 및 호출
def my_function():
  print("Hello")
  print("Bye")

my_function()

# 로봇 동작
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
turn_left()
move()
turn_right()
move()
turn_right()
move()
turn_left()
move()

# 반복문으로 장애물 넘기
def turn_right():
    turn_left()
    turn_left()
    turn_left()

for n in range(6):
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

# while문
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
  
while not at_goal():
    jump()

# 반복문을 이용한 랜덤 장애물 넘기
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
  
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()

# 반복문을 이용한 랜덤 위치 및 높이 장애물 넘기
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    while not right_is_clear():
        move()
    turn_right()
    move()
    turn_right()
    while not wall_in_front():
        move()
    turn_left()
  
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()

# 미로찾기
def turn_right():
    turn_left()
    turn_left()
    turn_left()
  
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
   