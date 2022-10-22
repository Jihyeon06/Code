0# MySQL 모듈
import pymysql
import time
# 키보드 모듈
from pynput import keyboard
import json
import threading

with open('EquipmentList.json', 'rt', encoding='UTF8') as data_file:
    data = json.load(data_file)

host = "localhost"
port = 0000
database = "dbname"
username = "root"
password = "pw"
















# 위에부터는 민감정보 ^^^^

conn = pymysql.connect(host=host, user=username, passwd=password, db=database, port=port, use_unicode=True, charset='utf8')
cursor = conn.cursor(pymysql.cursors.DictCursor)

MapSize = [80, 8]
PosMaxXInt = MapSize[0] - 1
PosMaxYInt = MapSize[1] - 1
PosXInt = -1
PosYInt = -1

PosXarr = []
PosYarr = []
PosXYarr = []

while PosMaxXInt > PosXInt:
    PosXInt = PosXInt + 1
    PosXarr = PosXarr + [PosXInt]

while PosMaxYInt > PosYInt:
    PosYInt = PosYInt + 1
    PosYarr = PosYarr + [PosYInt]

for PMY in PosYarr:
    for PMX in PosXarr:
        PosXYarr = PosXYarr + ['None', (PMX, PMY)]

pos = PosXYarr

FREEWORLD_TEXT = """








    ============================================================================================================================
    ∥  :::::::::: :::::::::  :::::::::: ::::::::::                 :::       :::  ::::::::  :::::::::  :::        :::::::::    ∥
    ∥  :+:        :+:    :+: :+:        :+:                        :+:       :+: :+:    :+: :+:    :+: :+:        :+:    :+:   ∥
    ∥  +:+        +:+    +:+ +:+        +:+                        +:+       +:+ +:+    +:+ +:+    +:+ +:+        +:+    +:+   ∥
    ∥  :#::+::#   +#++:++#:  +#++:++#   +#++:++#    +#++:++#++:++  +#+  +:+  +#+ +#+    +:+ +#++:++#:  +#+        +#+    +:+   ∥
    ∥  +#+        +#+    +#+ +#+        +#+                        +#+ +#+#+ +#+ +#+    +#+ +#+    +#+ +#+        +#+    +#+   ∥
    ∥  #+#        #+#    #+# #+#        #+#                         #+#+# #+#+#  #+#    #+# #+#    #+# #+#        #+#    #+#   ∥
    ∥  ###        ###    ### ########## ##########                   ###   ###    ########  ###    ### ########## #########    ∥
    ============================================================================================================================"""

Clear_TEXT = """

""" * 16


Player_Now_Number = "Null"
Player_Now_Nickname = "Null"
Player_Now_Level = 1
Player_Now_Money = 0

def Load_Login_Form():
    print(FREEWORLD_TEXT + """
    1. 본인의 아이디를 입력하여 주세요. (메인화면 : 엔터)
    ============================================================================================================================""")
    id_input = input("    값 : ")
    if id_input:
        try:
            get_id_query = "select * from member_account where account_id = %s"
            cursor.execute(get_id_query, id_input)  # 실행할 query문 넣기
            rs = cursor.fetchall()  # query문 실행해서 데이터 가져오기
            for id_v in rs:
                id_data = id_v["account_id"]

            if id_input == id_data:
                try:
                    print(FREEWORLD_TEXT + """
    2. 해당 비밀번호를 입력하여 주세요.
    ============================================================================================================================""")
                    password_input = input("    값 : ")

                    get_password_query = "select * from member_account where account_id = %s"
                    cursor.execute(get_password_query, password_input)  # 실행할 query문 넣기
                    rs = cursor.fetchall()  # query문 실행해서 데이터 가져오기
                    for password_v in rs:
                        password_data = password_v["account_password"]

                    if password_input == password_data:
                        print(FREEWORLD_TEXT + """
    로그인 성공, 잠시 뒤 이동됩니다. (아이디 : """ + id_input + """ | 비밀번호 : """ + password_input + """)
    ============================================================================================================================""")
                        for info_v in rs:
                            global Player_Now_Number
                            global Player_Now_Nickname
                            Player_Now_Number = info_v["account_number"]
                            Player_Now_Nickname = info_v["account_nickname"]
                        time.sleep(1)

                        conn.commit()
                    else:
                        print(FREEWORLD_TEXT + """
    해당 비밀번호는 존재하지 않습니다.
    ============================================================================================================================""")
                        time.sleep(1)
                        Load_Login_Form()
                except Exception as e:
                    print(FREEWORLD_TEXT + """
    해당 비밀번호는 존재하지 않습니다.
    ============================================================================================================================""")
                    time.sleep(1)
                    Load_Login_Form()
            else:
                print(FREEWORLD_TEXT + """
    해당 아이디는 존재하지 않습니다.
    ============================================================================================================================""")
                time.sleep(1)
                Load_Login_Form()
        except Exception as e:
            print(FREEWORLD_TEXT + """
    해당 아이디는 존재하지 않습니다.
    ============================================================================================================================""")
            time.sleep(1)
            Load_Login_Form()
    else:
        Load_Menu_Form()

def Load_Register_Form():
    print(FREEWORLD_TEXT + """
    2. 회원가입 할 닉네임을 입력하세요. (메인화면 : 엔터)
    ============================================================================================================================""")
    nickname_input = input("    값 : ")
    if nickname_input:
        print(FREEWORLD_TEXT + """
    2. 회원가입 할 해당 아이디를 입력하세요. (메인화면 : 엔터)
    ============================================================================================================================""")
        id_input = input("    값 : ")

        if id_input:
            print(FREEWORLD_TEXT + """
    3. 회원가입 할 해당 비밀번호를 입력하세요. (메인화면 : 엔터)
    ============================================================================================================================""")
            password_input = input("    값 : ")
            if password_input:
                try:
                    get_password_query = "insert into member_account (account_nickname, account_id, account_password) VALUES('" + nickname_input + "', '" + id_input + "', '" + password_input + "')"
                    cursor.execute(get_password_query)  # 실행할 query문 넣기
                    rs = cursor.fetchall()  # query문 실행해서 데이터 가져오기

                    print(FREEWORLD_TEXT + """
    회원가입 성공, 잠시 뒤 이동됩니다. (닉네임 : """ + nickname_input + """ 아이디 : """ + id_input + """ | 비밀번호 : """ + password_input + """)
    ============================================================================================================================""")
                    time.sleep(3)

                    conn.commit()
                    Load_Menu_Form()
                except Exception as e:
                    print(FREEWORLD_TEXT + """
    닉네임이나 아이디가 이미 존재합니다.
    ============================================================================================================================""")
                    time.sleep(1)
                    Load_Login_Form()

                    conn.commit()
            else:
                Load_Menu_Form()
        else:
            Load_Menu_Form()
    else:
        Load_Menu_Form()

def Load_Menu_Form():
    print(FREEWORLD_TEXT + """
    1번 키를 눌러 로그인을 하실 수 있습니다.
    2번 키를 눌러 회원가입을 하실 수 있습니다.
    3번 키를 눌러 비밀번호 변경을 하실 수 있습니다.
    4번 키를 눌러 회원정보 탈퇴을 하실 수 있습니다.
    5번 키를 눌러 서버 랭킹을 확인 하실 수 있습니다.
    ESC 키를 눌러 종료 하실 수 있습니다.
    ============================================================================================================================""")
    chat_input = input("    값 : ")
    if chat_input == "1":
        Load_Login_Form()
    elif chat_input == "2":
        Load_Register_Form()
    elif chat_input == "3":
        print("3번")
    elif chat_input == "4":
        print("4번")
    elif chat_input == "5":
        print("5번")
    else:
        Load_Menu_Form()

Load_Menu_Form() # 메인메뉴 표시

Player_Max_Health = 100
Player_Now_Health = 100

Player_Max_Energy = 500
Player_Now_Energy = 500

def Reload_Player_Data():
    get_info_query = "select * from member_account where account_number = '" + str(Player_Now_Number) + "'"
    cursor.execute(get_info_query)  # 실행할 query문 넣기
    rs = cursor.fetchall()  # query문 실행해서 데이터 가져오기
    for info_v in rs:
        global Player_Now_Nickname
        global Player_Now_Level
        global Player_Now_Money

        Player_Now_Nickname = info_v["account_nickname"]
        Player_Now_Level = info_v["account_level"]
        Player_Now_Money = info_v["account_money"]

        global Player_Now_Weapon_name
        global Player_Now_Armor_hat_name
        global Player_Now_Armor_top_name
        global Player_Now_Armor_bottom_name
        global Player_Now_Armor_shoes_name

        Player_Now_Weapon_name = info_v["weapon_name"]
        Player_Now_Armor_hat_name = info_v["armor_hat_name"]
        Player_Now_Armor_top_name = info_v["armor_top_name"]
        Player_Now_Armor_bottom_name = info_v["armor_bottom_name"]
        Player_Now_Armor_shoes_name = info_v["armor_shoes_name"]

    conn.commit()

Reload_Player_Data()

Weapon_List = data['weapon']
Armor_hat_List = data['armor']['hat']
Armor_top_List = data['armor']['top']
Armor_bottom_List = data['armor']['bottom']
Armor_shoes_List = data['armor']['shoes']
Player_stats_Damage = 30
Player_stats_Defense = 30

Player_Now_Weapon_Damage = data['weapon'].get(Player_Now_Weapon_name)["Damage"] + data['armor']['hat'].get(Player_Now_Armor_hat_name)["Damage"] + data['armor']['top'].get(Player_Now_Armor_top_name)["Damage"] + data['armor']['bottom'].get(Player_Now_Armor_bottom_name)["Damage"] + data['armor']['shoes'].get(Player_Now_Armor_shoes_name)["Damage"]
Player_Now_Weapon_Defense = data['weapon'].get(Player_Now_Weapon_name)["Damage"] + data['armor']['hat'].get(Player_Now_Armor_hat_name)['Defense'] + data['armor']['top'].get(Player_Now_Armor_top_name)['Defense'] + data['armor']['bottom'].get(Player_Now_Armor_bottom_name)['Defense'] + data['armor']['shoes'].get(Player_Now_Armor_shoes_name)['Defense']

Player_Now_Damage = (Player_stats_Damage * 10) + Player_Now_Weapon_Damage # 공격력 계산
Player_Now_Defense = (Player_stats_Defense * 10) + Player_Now_Weapon_Defense # 방어력 계산

Player_Now_Ranking = "1 등"

def Get_PosXYArr(x, y): # 좌표로 찾기
    return pos.index((x, y))

def Get_PosNameArr(name): # 이름으로 찾기
    return pos.index(name)

# 맵로드
def Load_Map():
    print(Clear_TEXT)
    a1 = (len(pos) / 2) / MapSize[0]
    a2 = len(pos) / 2 / MapSize[1]
    line = ''
    a4 = 0
    apos = 0
    while a1 > 0: #맵의 Y크기 만큼 반복
        a4 = 0
        line = ''
        while a2 > a4: # X만큼 반복
            apos = Get_PosXYArr(a4, (a1 - 1))
            m = pos[apos - 1]
            if m == "None":
                line = line + "\033[30m░"
            elif m == "Player":
                line = line + "\033[94m▒\033[30m"
            elif m == "Monster":
                line = line + "\033[91m▒\033[30m"
            elif m == "Attack":
                line = line + "\033[93m▒\033[30m"
            a4 = a4 + 1
        a1 = a1 - 1
        print(line)

def Load_Info1():
    print('\033[41m' + "체력 : " + ("%03d" % Player_Max_Health) + " | " + ("%03d" % Player_Now_Health) + '\033[0m' + "   " + '\033[44m' + "마나 : " + ("%03d" % Player_Max_Energy) + " | " + ("%03d" % Player_Now_Energy) + '\033[0m' + "   " + '\033[43m' + "페소 : " + ("%010d" % Player_Now_Money) + "$" + '\033[0m' + "   " + '\033[42m' + "레벨 : " + ("%03d" % Player_Now_Level) + '\033[0m')

def Load_Info2():
    print("닉네임 : " + Player_Now_Nickname + "   " + "순위 : " + Player_Now_Ranking)
    print("공격력 : " + ("%04d" % Player_Now_Damage) + "   " + "방어력 : " + ("%04d" % Player_Now_Defense))
    print("무기 : " + data['weapon'].get(Player_Now_Weapon_name)["Name"] + "   " + "방어구 : " + data['armor']['hat'].get(Player_Now_Armor_hat_name)['Name'] + " | " + data['armor']['top'].get(Player_Now_Armor_top_name)['Name'] + " | " + data['armor']['bottom'].get(Player_Now_Armor_bottom_name)['Name'] + " | " + data['armor']['shoes'].get(Player_Now_Armor_shoes_name)['Name'])

def Load_Info():
    Load_Map()  # 맵로드 시키기
    Load_Info1()
    Load_Info2()
    threading.Timer(0.3, Load_Info).start()  # 매번 불러오기

pos[(Get_PosXYArr(60, 0)) - 1] = "Player" # 플레이어 시작위치
pos[(Get_PosXYArr(5, 0)) - 1] = "Monster" # 몬스터 시작위치

Load_Info()

def Left_Sensor(player): # 왼쪽에 조형물, 몬스터, 벽이 있는지 확인
    try:
        if pos[Get_PosXYArr(pos[player + 1][0] - 1, pos[player + 1][1]) - 1] == "None": # 왼쪽
            return True
        else:
            return False
    except:
        return False

def Right_Sensor(player): # 오른쪽에 조형물, 몬스터, 벽이 있는지 확인
    try:
        if pos[Get_PosXYArr(pos[player + 1][0] + 1, pos[player + 1][1]) - 1] == "None": # 오른쪽
            return True
        else:
            return False
    except:
        return False

def Up_Sensor(player):  # 위쪽에 조형물, 몬스터, 벽이 있는지 확인
    try:
        if pos[Get_PosXYArr(pos[player + 1][0], pos[player + 1][1] + 1) - 1] == "None":
            return True
        else:
            return False
    except:
        return False

def Down_Sensor(player):  # 아래에 조형물이 있는지
    try:
        if pos[Get_PosXYArr(pos[player + 1][0], pos[player + 1][1] - 1) - 1] == "None":
            return True
        else:
            return False
    except:
        return False

def Left_Attack_Sensor(player):  # 왼쪽 위 오른쪽 조형물이 있는지
    try:
        if Left_Sensor(player):
            return True
        else:
            return False
    except:
        return False

def Right_Attack_Sensor(player):  # 왼쪽 위 오른쪽 조형물이 있는지
    try:
        if Right_Sensor(player):
            return True
        else:
            return False
    except:
        return False

def Up_Attack_Sensor(player):  # 왼쪽 위 오른쪽 조형물이 있는지
    try:
        if Up_Sensor(player):
            return True
        else:
            return False
    except:
        return False

def Move_Left():
    player = Get_PosNameArr("Player")
    if Left_Sensor(player):
        pos[Get_PosXYArr(pos[player + 1][0] - 1, pos[player + 1][1]) - 1] = "Player"
        pos[player] = "None"

def Move_Right():
    player = Get_PosNameArr("Player")
    if Right_Sensor(player):
        pos[Get_PosXYArr(pos[player + 1][0] + 1, pos[player + 1][1]) - 1] = "Player"
        pos[player] = "None"

def Move_Up():
    player = Get_PosNameArr("Player")
    if Up_Sensor(player):
        pos[Get_PosXYArr(pos[player + 1][0], pos[player + 1][1] + 1) - 1] = "Player"
        pos[player] = "None"

def Move_Down():
    player = Get_PosNameArr("Player")
    if Down_Sensor(player):
        pos[Get_PosXYArr(pos[player + 1][0], pos[player + 1][1] - 1) - 1] = "Player"
        pos[player] = "None"

def Attack():
    player = Get_PosNameArr("Player")
    if Left_Attack_Sensor(player):
        pos[Get_PosXYArr(pos[player + 1][0] - 1, pos[player + 1][1]) - 1] = "Attack"
    if Right_Attack_Sensor(player):
        pos[Get_PosXYArr(pos[player + 1][0] + 1, pos[player + 1][1]) - 1] = "Attack"
    if Up_Attack_Sensor(player):
        pos[Get_PosXYArr(pos[player + 1][0], pos[player + 1][1] + 1) - 1] = "Attack"

    time.sleep(0.3)
    pos[Get_PosXYArr(pos[player + 1][0] - 1, pos[player + 1][1]) - 1] = "None"
    pos[Get_PosXYArr(pos[player + 1][0] + 1, pos[player + 1][1]) - 1] = "None"
    pos[Get_PosXYArr(pos[player + 1][0], pos[player + 1][1] + 1) - 1] = "None"

cooldown_L = True
cooldown_R = True
cooldown_U = True
cooldown_D = True
cooldown_A = True
cooldown_time = 0.4

def on_press(key):
    try:
        global cooldown_L
        global cooldown_R
        global cooldown_U
        global cooldown_D
        global cooldown_A
        print('Key released: {0}'.format(key))
        if key == keyboard.Key.left and cooldown_L:
            cooldown_L = False
            Move_Left()
            time.sleep(cooldown_time)
            cooldown_L = True
        elif key == keyboard.Key.right and cooldown_R:
            cooldown_R = False
            Move_Right()
            time.sleep(cooldown_time)
            cooldown_R = True
        elif key == keyboard.Key.up and cooldown_U:
            cooldown_U = False
            Move_Up()
            time.sleep(cooldown_time)
            cooldown_U = True
        elif key == keyboard.Key.down and cooldown_D:
            cooldown_D = False
            Move_Down()
            time.sleep(cooldown_time)
            cooldown_D = True
        elif key == keyboard.Key.space and cooldown_A:
            cooldown_A = False
            Attack()
            time.sleep(cooldown_time)
            cooldown_A = True

    except AttributeError:
        print('special key pressed: {0}'.format(key))

def on_release(key):
    #print('Key released: {0}'.format(key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

with keyboard.Listener(
    on_press=on_press,
    on_release=on_release
) as listener:
    listener.join()

conn.close()

































