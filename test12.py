print('โปรเเกรมคำณวนค่าผ่านทางมอเตอร์เวย์')
print('\tรถยนต์ 4 ล้อ   กด1')
print('\tรถยนต์ 6 ล้อ   กด2')
print('\tรถยนต์มากกว่า 6 ล้อ  กด 3\n')
list1 = ['ลาดกระบัง-->บางบ่อ:25บาท','ลาดกระบัง-->บางประกง:30บาท','ลาดกระบัง-->พนัสนิคม:45บาท','ลาดกระบัง-->บ้านบึ้ง:55บาท','ลาดกระบัง-->บางพระ:60บาท']
list2 = ['ลาดกระบัง-->บางบ่อ:40บาท','ลาดกระบัง-->บางประกง:45บาท','ลาดกระบัง-->พนัสนิคม:75บาท','ลาดกระบัง-->บ้านบึ้ง:90บาท','ลาดกระบัง-->บางพระ:100บาท']
list3 = ['ลาดกระบัง-->บางบ่อ:60บาท','ลาดกระบัง-->บางประกง:70บาท','ลาดกระบัง-->พนัสนิคม:110บาท','ลาดกระบัง-->บ้านบึ้ง:130บาท','ลาดกระบัง-->บางพระ:140บาท'] 
car = int(input('\tเลือกประเภทยานพาหนะ : '))
if car == 1 :
    print('\tค่าบริการรถยนต์ 4 ล้อ')
    for x in list1:
        print('\n',x)
elif car == 2 :
    print('\tค่าบริการรถยนต์ 6 ล้อ')
    for x in list2:
        print('\n',x)
elif car == 3:
    print('\tค่าบริการรถยนต์มากกว่า 6 ล้อ')
    for x in list3:
        print('\n',x)       