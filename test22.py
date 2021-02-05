import os
choice = 0
listfood = [0,0,0,0,0,]
pick = 0
def menu():
    global choice
    print('\tโปรแกรมร้านผัดไทเเสนอร่อย\n','1.แสดงรายการอาหาร\n 2.หยิบอาหารเข้าตระกร้า\n 3.แสดงรายจำนวนและราคาของอาหารที่หยิบ\n 4.หยิบอาหารออกจากตะกร้า\n 5.ปิดโปรแกรม')
    choice = input('กรุณาเลือกทำรายการ : ')
    screen_clear()

def showmenu(): 
    print('\tรายการอาหารผัดไท')
    print('\t1.ผัดไท 45 บาท\n','\t2.ผัดไทกุ้งสด 50 บาท\n','\t3.ผัดไทรวม 55 บาท\n','\t4.ผัดไททะเล 50 บาท\n','\t5.ผัดไทพิเศษ 50 บาท')

def pickmenu():
    global pick
    print('\tรายการอาหาร\n 1.ผัดไท\n 2.ผัดไทกุ้งสด\n 3.ผัดไทรวม\n 4.ผัดไททะเล\n 5.ผัดไทพิเศษ')
    pick = int(input('เลือกหยิบอาหารหมายเลข :'))
    if pick == 1:
        listfood[0] += 1
    elif pick == 2:
        listfood[1] += 1
    elif pick == 3:
        listfood[2] += 1
    elif pick == 4:
        listfood[3] += 1
    elif pick == 5:
        listfood[4] += 1
    screen_clear()

def showuserpick():
    list_score = ['ผัดไท','ผัดไทกุ้งสด','ผัดไทรวม','ผัดไททะเล','ผัดไทพิเศษ']
    list_price = [45,50,55,50,50]
    print('{0:-<13}{1:-<13}{2:-<13}{3}'.format('อาหาร','ราคา','จำนวน','ราคารวม'))
    for i in range(0,5):
        print('{0:-<13}{1:-<13}{2:-<13}{3}'.format(list_score[i],list_price[i],listfood[i],listfood[i]*list_price[i]))

def deletuserpick():
    print('\t\nรายการอาหาร\n 1.ผัดไท\n 2.ผัดไทกุ้งสด\n 3.ผัดไทรวม\n 4.ผัดไททะเล\n 5.ผัดไทพิเศษ')
    depick = int(input('เลือกลำดับอาหารที่จะหยิบออก หรือพิมพ์ -1 เพื่อออก'))
    if depick == 1:
        listfood[0] -= 1
    elif depick == 2:
        listfood[1] -= 1
    elif depick == 3:
        listfood[2] -= 1
    elif depick == 4:
        listfood[3] -= 1
    elif depick == 5:
        listfood[4] -= 1

def screen_clear():
    clearscreen = os.system('cls')

while True:
    menu()
    if choice == '1':
        screen_clear()
        showmenu()
    elif choice == '2':
        screen_clear()
        pickmenu()
    elif choice == '3':
        screen_clear()
        showuserpick()
    elif choice == '4':
        deletuserpick()
        screen_clear()
    elif choice == '5':
        c = input('ต้องการใช้โปรแกรมต่อหรือไม่ y/n: ')
        if c.lower() == 'y':
            screen_clear()
        elif c.lower() == 'n':
            screen_clear()
            break
