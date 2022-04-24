import time
import random

print("5개의 메뉴를 추가해주세요! 5개가 입력되면 오늘의 메뉴를 추천해드려요.")
print("동일한 메뉴는 안돼요!\n")
menu_list=[]

while True:
    menu = input("메뉴 추가: ")
    menu_list.append(menu)


    if len(menu_list) != len(set(menu_list)):
        print("이미 있는 메뉴에요! 다른 메뉴를 입력해주세요.")
        menu_list.pop()
        print("현재 메뉴 수 = ", len(menu_list),"\n")
    
    elif len(menu_list)==5:
        print("현재 메뉴 수 = ", len(menu_list),"\n")
        break
    
    else:

        print("현재 메뉴 수 = ", len(menu_list),"\n")
    

print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("\n")
print(menu_list)
print("과연 오늘의 메뉴는?")
print("\n")

print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("\n")
today_menu = random.choice(menu_list)
print("오늘의 메뉴는 ", menu_list.index(today_menu)+1, "번째 메뉴," ,today_menu, "입니다.")