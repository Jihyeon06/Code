import random

def start():
  while True:
    print("[ Choose the difficulty level! ]")
    print("[0] God       : This is the answer of 1-10 digits plus 1-10 digits.")
    print("[5] Very hard : This is the answer of 1-5 digits plus 1-5 digits.")
    print("[4] Hard      : This is the answer of 1-4 digits plus 1-4 digits.")
    print("[3] Normal    : This is the answer of 1-3 digits plus 1-3 digits.")
    print("[2] Easy      : This is the answer of 1-2 digits plus 1-2 digits.")
    print("[1] Very easy : This is the answer of 1 digits plus 1 digits.")
    print("* If you want to go to the settings menu during the game, answer input '/' Please *")
    answer = input("answer : ")
    if answer.lower() == "God" or answer == "0":
      difficulty = 9999999999
    elif answer.lower() == "very hard" or answer == "5":
      difficulty = 99999
    elif answer.lower() == "hard" or answer == "4":
      difficulty = 9999
    elif answer.lower() == "normal" or answer == "3":
      difficulty = 999
    elif answer.lower() == "easy" or answer == "2":
      difficulty = 99
    elif answer.lower() == "very easy" or answer == "1":
      difficulty = 9
    else:
      print('Unknown answer. Please again input your answer.')
      print()
      continue
    
    print()
    game(difficulty)


def game(n):
  try_number = 0
  right_answer_number = 0
  operator = "+" # 기본값 +
  while True:
    if random.choice([True, False]): # True 라면
      operator = "+"
    else: # 아니라면
      operator = "-" 
    
    x, y = random.randrange(1, n), random.randrange(1, n)
    calculation = f"{x} {operator} {y}" 
      
    print(f"[{x}] {operator} [{y}] = [?]")
    answer = input("answer : ")
    
    if answer == str(eval(calculation)):
      print("Right answer!")
      right_answer_number += 1
    elif answer == "/":
      print("Go to the settings menu.")
      print(f"Try Number          : {try_number}")
      print(f"Right answer Number : {right_answer_number}")
      print(f"Wrong answer Number : {try_number - right_answer_number}")
      print(f"Correct answer rate : {(100 / try_number) * right_answer_number:.2f} %")
      print()
      break
    else:
      print('Wrong answer.')
      print(f'correct answer : [{eval(calculation)}]')

    try_number += 1
    print()
      
start() # 게임시작
