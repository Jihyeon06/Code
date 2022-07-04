import time

# 변수 저장
isrule = "O"
startrule = "O"
PLAYER_STONE = 'O'
COMPUTER_STONE = 'X'
first = "X"

# 게임 정보
def GameInfo():
	ConsoleClen()
	print("┏━━━━━━━━━━━┓")
	print("┃ [ \033[93mT-T-T\033[0m ] ┃")
	print("┠───┬───┬───┨")
	print("┃ 7 │ 8 │ 9 ┃")
	print("┠───┼───┼───┨")
	print("┃ 4 │ 5 │ 6 ┃")
	print("┠───┼───┼───┨")
	print("┃ 1 │ 2 │ 3 ┃")
	print("┠───┴───┴───┨")
	print("┃ [ \033[93mENTER\033[0m ] ┃")
	print("┗━━━━━━━━━━━┛")
	

# 콘솔 청소
def ConsoleClen():
	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

#보드에서 startrule('O' 또는 'X')가 연속해서 3개 놓여졌는지 여부(True 또는 False)를 리턴한다.
def Game_Winner(number, startrule, numbercolor):
	#가로 세 행 확인
	for i in [1, 4, 7]:
		if number[i] == startrule and number[i + 1] == startrule and number[i + 2] == startrule:

			if startrule == "O":
				numbercolor[i] = "\033[94m \033[103m" + startrule + "\033[0m"
				numbercolor[i + 1] = "\033[94m \033[103m" + startrule + "\033[0m"
				numbercolor[i + 2] = "\033[94m \033[103m" + startrule + "\033[0m"
			elif startrule == "X":
				numbercolor[i] = "\033[91m \033[103m" + startrule + "\033[0m"
				numbercolor[i + 1] = "\033[91m \033[103m" + startrule + "\033[0m"
				numbercolor[i + 2] = "\033[91m \033[103m" + startrule + "\033[0m"

			return True

	#세로 세 열 확인
	for i in [1, 2, 3]:
		if number[i] == startrule and number[i + 3] == startrule and number[i + 6] == startrule:

			if startrule == "O":
				numbercolor[i] = "\033[94m \033[103m" + startrule + "\033[0m"
				numbercolor[i + 3] = "\033[94m \033[103m" + startrule + "\033[0m"
				numbercolor[i + 6] = "\033[94m \033[103m" + startrule + "\033[0m"
			elif startrule == "X":
				numbercolor[i] = "\033[91m \033[103m" + startrule + "\033[0m"
				numbercolor[i + 3] = "\033[91m \033[103m" + startrule + "\033[0m"
				numbercolor[i + 6] = "\033[91m \033[103m" + startrule + "\033[0m"

			return True

	#대각선(오른쪽 위에서 왼쪽 아래)
	if number[1] == startrule and number[5] == startrule and number[9] == startrule:

		if startrule == "O":
			numbercolor[1] = "\033[94m \033[103m" + startrule + "\033[0m"
			numbercolor[5] = "\033[94m \033[103m" + startrule + "\033[0m"
			numbercolor[9] = "\033[94m \033[103m" + startrule + "\033[0m"
		elif startrule == "X":
			numbercolor[1] = "\033[91m \033[103m" + startrule + "\033[0m"
			numbercolor[5] = "\033[91m \033[103m" + startrule + "\033[0m"
			numbercolor[9] = "\033[91m \033[103m" + startrule + "\033[0m"

		return True

	#대각선(왼쪽 위에서 오른쪽 아래)
	if number[3] == startrule and number[5] == startrule and number[7] == startrule:

		if startrule == "O":
			numbercolor[3] = "\033[94m \033[103m" + startrule + "\033[0m"
			numbercolor[5] = "\033[94m \033[103m" + startrule + "\033[0m"
			numbercolor[7] = "\033[94m \033[103m" + startrule + "\033[0m"
		elif startrule == "X":
			numbercolor[3] = "\033[91m \033[103m" + startrule + "\033[0m"
			numbercolor[5] = "\033[91m \033[103m" + startrule + "\033[0m"
			numbercolor[7] = "\033[91m \033[103m" + startrule + "\033[0m"

		return True

	return False

#플레이어로부터 위치를 입력받기
def getPlayerMove(number, startrule, numbercolor):
	while True:
		if startrule == "O":
			selectmessage = input("[ \033[94mO\033[0m ] 놓을곳을 선택해주세요. : ")
		elif startrule == "X":
			selectmessage = input("[ \033[91mX\033[0m ] 놓을곳을 선택해주세요. : ")
		if len(selectmessage) == 1 and '1' <= selectmessage <= '9':
			pos = int(selectmessage)
			if number[pos] == '-':
				number[pos] = startrule

				if startrule == "O":
					numbercolor[int(selectmessage)] = "\033[94m" + startrule + "\033[0m"
				elif startrule == "X":
					numbercolor[int(selectmessage)] = "\033[91m" + startrule + "\033[0m"
				break
			else:
				Loadnumber(numbercolor)
				print("[ \033[95m!\033[0m ] 비어있는 칸을 선택하여 주세요.")
		else:
			Loadnumber(numbercolor)
			print("[ \033[95m!\033[0m ] 숫자는 1~9까지만 선택이 가능합니다.")

def getComputerMove(number, rule, numbercolor):
	if rule == "O":
		print("")
		print("[ \033[94mO\033[0m ] 놓을곳을 선택하고 있습니다.")
	elif rule == "X":
		print("")
		print("[ \033[91mX\033[0m ] 놓을곳을 선택하고 있습니다.")
	time.sleep(1.5)
	#컴퓨터가 두면 이길 위치를 찾아둔다.
	for i in range(1, 10):
		if number[i] == '-':
			copynumber = number[:]
			copynumber[i] = COMPUTER_STONE
			if Game_Winner(copynumber, COMPUTER_STONE, numbercolor):
				number[i] = rule
				if rule == "O":
					numbercolor[i] = "\033[94m" + rule + "\033[0m"
				elif rule == "X":
					numbercolor[i] = "\033[91m" + rule + "\033[0m"
				return

	#플레이어가 두면 이길 위치를 찾아둔다.
	for i in range(1, 10):
		if number[i] == '-':
			copynumber = number[:]
			copynumber[i] = PLAYER_STONE
			if Game_Winner(copynumber, PLAYER_STONE, numbercolor):
				number[i] = rule
				if rule == "O":
					numbercolor[i] = "\033[94m" + rule + "\033[0m"
				elif rule == "X":
					numbercolor[i] = "\033[91m" + rule + "\033[0m"
				return

	#앞에서부터 빈자리를 찾아 둡니다.
	for i in range(1, 10):
		if number[i] == '-':
			number[i] = rule
			if rule == "O":
				numbercolor[i] = "\033[94m" + rule + "\033[0m"
			elif rule == "X":
				numbercolor[i] = "\033[91m" + rule + "\033[0m"
			break

#누가 먼저 시작할지 랜덤하게 정하고, 정해진 순서('O' 또는 'X')를 리턴한다.
def whoIsFirst():
	global first

	if first != "O":
		print("[ \033[94m플레이어\033[0m ] 부터 시작합니다.")
		first = "O"

	elif first != "X":
		print("[ \033[91m인공지능\033[0m ] 부터 시작합니다.")
		first = "X"
	return first
		
# 게임 시작 (싱글_친구 플레이)
def Game_Single_Friend_Start():
	global startrule # 전역변수
	global result_Single_Friend_List
	number = ['-'] * 10 # 위치 저장하기 (진값) [System 용]
	numbercolor = ['-'] * 10 # 위치 색상 (가값) [Print 용]
	Loadnumber(number) # 처음 기본 보드의 내용을 로드하기

	while True:
		getPlayerMove(number, startrule, numbercolor)
		Loadnumber(numbercolor)
		
		if Game_Winner(number, startrule, numbercolor):
			if startrule == "O":
				print("[ \033[94mO\033[0m ] 라운드가 종료되었습니다.")
				result_Single_Friend_List.append(startrule)

				print("")
				gamestartinput = input("[ \033[93mENTER\033[0m ]")

				GameStartStopIf()
			elif startrule == "X":
				print("[ \033[91mX\033[0m ] 라운드가 종료되었습니다.")
				result_Single_Friend_List.append(startrule)

				print("")
				gamestartinput = input("[ \033[93mENTER\033[0m ]")

				GameStartStopIf()
			return startrule

		if numberOfstartrule(number) >= 9:
			print("[ \033[93m-\033[0m ] 라운드가 종료되었습니다.")
			result_Single_Friend_List.append("-")

			print("")
			gamestartinput = input("[ \033[93mENTER\033[0m ]")

			GameStartStopIf()
			return "-"
			
		if startrule == "O":
			startrule = "X"
		elif startrule == "X":
			startrule = "O"

# 게임 시작 (싱글_인공지능 플레이)
def Game_Single_Ai_Start():
	global PLAYER_STONE # 전역변수
	global COMPUTER_STONE
	global result_Single_Ai_List
	number = ['-'] * 10 # 위치 저장하기 (진값) [System 용]
	numbercolor = ['-'] * 10 # 위치 색상 (가값) [Print 용]
	Loadnumber(number) # 처음 기본 보드의 내용을 로드하기
	currentStone = whoIsFirst()
	while True:
		if currentStone == PLAYER_STONE:
			getPlayerMove(number, PLAYER_STONE, numbercolor) 
			Loadnumber(numbercolor)
			print("")
			
			if Game_Winner(number, PLAYER_STONE, numbercolor):
				print("[ \033[94mO\033[0m ] 라운드가 종료되었습니다.")
				result_Single_Ai_List.append(PLAYER_STONE)

				print("")
				gamestartinput = input("[ \033[93mENTER\033[0m ]")

				GameStartStopIf()
				return PLAYER_STONE

			currentStone = COMPUTER_STONE

		else:
			getComputerMove(number, COMPUTER_STONE, numbercolor)
			Loadnumber(numbercolor)

			if Game_Winner(number, COMPUTER_STONE, numbercolor):
				print("[ \033[91mX\033[0m ] 라운드가 종료되었습니다.")
				result_Single_Ai_List.append(COMPUTER_STONE)

				print("")
				gamestartinput = input("[ \033[93mENTER\033[0m ]")

				GameStartStopIf()
				return COMPUTER_STONE
				
			currentStone = PLAYER_STONE

		if numberOfstartrule(number) >= 9:
			print("[ \033[93m-\033[0m ] 라운드가 종료되었습니다.")
			result_Single_Ai_List.append("-")
			
			print("")
			gamestartinput = input("[ \033[93mENTER\033[0m ]")

			GameStartStopIf()
			return '-'

# 보드의 내용을 로드하기
def Loadnumber(numbercolor):
	ConsoleClen()
	print("┏━━━━━━━━━━━┓")
	print("┃ [ \033[93mT-T-T\033[0m ] ┃")
	print("┠───┬───┬───┨")
	print("┃ " + numbercolor[7] + " │ " + numbercolor[8] + " │ " + numbercolor[9] + " ┃")
	print("┠───┼───┼───┨")
	print("┃ " + numbercolor[4] + " │ " + numbercolor[5] + " │ " + numbercolor[6] + " ┃")
	print("┠───┼───┼───┨")
	print("┃ " + numbercolor[1] + " │ " + numbercolor[2] + " │ " + numbercolor[3] + " ┃")
	print("┠───┴───┴───┨")
	print("┃ [ \033[93mENTER\033[0m ] ┃")
	print("┗━━━━━━━━━━━┛")
	print("")

# 보드에 놓여진 돌의 개수를 리턴하기
def numberOfstartrule(number):
	n = 0
	for c in number:
		if c != '-':
			n = n + 1
	return n

# 게임 시작/중지/변경 메뉴 선택
def GameStartStopIf():
	global startrule # 전역변수
	global PLAYER_STONE 
	global COMPUTER_STONE
	global isrule

	startrule = isrule

	while True:	
		ConsoleClen()
		GameInfo()
		print("")
		gamestartinput = input("[ \033[95m!\033[0m ] 게임을 시작하시겠습니까? (시작/중지/변경/전적) : ")
		if gamestartinput == "시작" or gamestartinput == "1":
			GameInfo()
			print("[ \033[95m!\033[0m ] 게임을 시작하시겠습니까? (시작/중지/변경/전적) : ")
			gamestartinput = input("(친구/인공지능) : ")
			if gamestartinput == "친구" or gamestartinput == "1":
				print("[ \033[93m친구 플레이\033[0m ] 게임을 시작합니다.")
				print("첫번째 턴 : [ \033[93m" + startrule + "\033[0m ]")
				Game_Single_Friend_Start()
				break
			elif gamestartinput == "인공지능" or gamestartinput == "2":
				print("[ \033[93m인공지능 플레이\033[0m ] 게임을 시작합니다.")
				print("첫번째 턴 : [ \033[93m" + startrule + "\033[0m ]")
				Game_Single_Ai_Start()
				break
		elif gamestartinput == "중지" or gamestartinput == "2":
			GameInfo()
			print("[ \033[95m!\033[0m ] 게임을 시작하시겠습니까? (시작/중지/변경/전적) : ")
			print("게임을 종료합니다.",end = "")
			break
		elif gamestartinput == "변경" or gamestartinput == "3":
			if startrule == "O":
				startrule = "X"
				isrule = "X"
			elif startrule == "X":
				startrule = "O"
				isrule = "O"

			print("이제부터 턴은 [ \033[93m" + startrule + "\033[0m ] 부터 시작 됩니다!")
		elif gamestartinput == "전적" or gamestartinput == "4":
			gamestartinput = input("(친구/인공지능) : ")
			if gamestartinput == "친구" or gamestartinput == "1":
				Game_Single_Friend_Result()
				break
			elif gamestartinput == "인공지능" or gamestartinput == "2":
				Game_Single_Ai_Result()
				break
		else:
			print("시작 혹은 중지를 입력하여 주세요.")

# 결과 보기	(친구 플레이)
result_Single_Friend_List = []
def Game_Single_Friend_Result():
	global result_Single_Friend_List
	print('[ 게임 결과 ]')
	for i in range(len(result_Single_Friend_List)):
		print("[ ", i+1, ':', end = ' ')
		if result_Single_Friend_List[i] == '-':
			print("\033[93m- 무\033[0m ]")
		else:
			if result_Single_Friend_List[i] == "O":
				print("\033[93mO 승\033[0m ]")
			elif result_Single_Friend_List[i] == "X":
				print("\033[93mX 승\033[0m ]")
		print("[ ", i+1, ":\033[93m ? 전\033[0m ]")

	print("")
	gamestartinput = input("[ \033[93mENTER\033[0m ]")
	GameStartStopIf()

# 결과 보기	(인공지능 플레이)
result_Single_Ai_List = []
def Game_Single_Ai_Result():
	global result_Single_Ai_List
	global PLAYER_STONE
	global COMPUTER_STONE

	print('[ 게임 결과 ]')
	print("[\033[94m", result_Single_Ai_List.count(PLAYER_STONE), '승\033[0m ]')
	print("[\033[91m", result_Single_Ai_List.count(COMPUTER_STONE), '패\033[0m ]')
	print("[\033[93m", result_Single_Ai_List.count('-'), '무\033[0m ]')

	print("")
	gamestartinput = input("[ \033[93mENTER\033[0m ]")
	GameStartStopIf()

# 초반 게임 메뉴 활성화
GameStartStopIf()