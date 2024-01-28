# 딕셔너리
programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.",
  "Function": "A piece of code that you can easily call over and over again.",
}

# 딕셔너리 key 검색
print(programming_dictionary["Bug"])

# 객체 추가
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

# 신규 딕셔너리 추가
empty_dictionary = {}

# programming_dictionary 딕셔너리 초기화
programming_dictionary = {}
print(programming_dictionary)

# Bug Key와 Value를 empty_dictionary에 적용
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)

# 딕셔너리에 반복문 적용
for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key])

# 미션) 등급 매기는 프로그램
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Heville": 62,
}

student_grades = {}

for name in student_scores:
  score = student_scores[name]
  if score >= 91 and score <= 100:
    student_grades[name] = "Outstanding"
  elif score >= 81 and score <= 90:
    student_grades[name] = "Exceeds Expectations"
  elif score >= 71 and score <= 80:
    student_grades[name] = "Acceptable"
  else:
    student_grades[name] = "Fail"    

print(student_grades)

# 리스트와 딕셔너리 중첩
capitals = {
  "France": "Paris",
  "Germany": "Berlin"
}

travel_log = {
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

travel_log = [
  {
    "country": "France", 
    "cities_visited": ["Paris", "Lille", "Dijon"], 
    "total_visits": 12
  },
  {
    "country": "Germany", 
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
    "total_visits": 5
  },
]

print(travel_log)

# 미션) 리스트 속 딕셔너리
country = input()
visits = int(input())
list_of_cities = eval(input())

travel_log = [
  {
    "country": "France", 
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"], 
  },
  {
    "country": "Germany", 
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"], 
  },
]

def add_new_country(name, times_visited, cities_visited):
  new_travel_log = {}
  new_travel_log["country"] = name
  new_travel_log["visits"] = times_visited
  new_travel_log["cities"] = cities_visited
  travel_log.append(new_travel_log)

add_new_country(country, visits, list_of_cities)

print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")

# 프로젝트
import os
from art import logo

print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    os.system('cls')