import sqlite3
conn = sqlite3.connect(r'D:\kittiwarit_pythone\Project2.py\project2..db')
c = conn.cursor()
#c.execute('''CREATE TABLE match(NO integer PRIMARY KEY AUTOINCREMENT,
#    Home varchar(1000) NOT NULL,
#    Score varchar(1000) NOT NULL,
#    Away varchar(1000) NOT NULL,
#    Stadium varchar(1000) NOT NULL)''')
#conn.commit()
#conn.close()

#c.execute('''CREATE TABLE name(No integer PRIMARY KEY AUTOINCREMENT,
#    Number varchar(1000) NOT NULL,
#    Name varchar(1000) NOT NULL)''')
#conn.commit(
#conn.close()
#c.execute('''ALTER TABLE name ADD COLUMN Team''')
#c.execute('''ALTER TABLE name ADD COLUMN Position''')
#c.execute('''ALTER TABLE match ADD COLUMN League''')
def menu_football():
    global choice
    print('========== บ้านผลบอล ==========')
    print('[1]  เพิ่มคู่เเข่งขันฟุตบอล')
    print('[2]  เเก้ไขคู่เเข่งขันฟุตบอล')
    print('[3]  เพิ่มรายชื่อนักเตะ')
    print('[4]  ลบรายชื่อนักเตะ')
    print('[5]  เเสดงรายชื่อนักเตะ')
    print('[6]  เเสดงคู่เเข่งขันฟุตบอล')
    choice = input('กรุณาเลือกรายการครับ :')

def showplayers():
    conn = sqlite3.connect(r'D:\kittiwarit_pythone\Project2.py\project2..db')
    c = conn.cursor()
    c.execute (''' SELECT * FROM name ''')
    result = c.fetchall()
    print('-'*60)
    print('\t\t\tPlayer')
    print('-'*60)
    print('{:>2}{:>12}{:>15}{:>14}{:>16}'.format('No','Number','Name','Team','Position'))
    for x in result :
        print('{:>1}{:>10}{:>18}{:>17}{:>10}'.format(x[0],x[1],x[2],x[3],x[4]))
def inmatch():
    conn = sqlite3.connect(r'D:\kittiwarit_pythone\Project2.py\project2..db')
    c = conn.cursor()
    h = str(input('ใส่ชื่อทีมเหย้า :'))
    s = str(input('ใส่ผลคะเเนน :'))
    a = str(input('ใส่ชื่อทีมเยือน :'))
    st = str(input('ใส่ชื่อสนาม :'))
    l = str(input('ใส่ลีกการเเข่งขันฟุตบอล :'))
    c.execute('''INSERT INTO match(Home,Score,Away,Stadium,League)
    VALUES(?,?,?,?,?)'''
    ,(h,s,a,st,l))
    conn.commit()
    print('เพิ่มการเเข่งขันสำเร็จเเล้ว')
    conn.close()

def showmatch():
    conn = sqlite3.connect(r'D:\kittiwarit_pythone\Project2.py\project2..db')
    c = conn.cursor()
    c.execute (''' SELECT * FROM match ''')
    result = c.fetchall()
    print('-'*60)
    print('\t\t\tMatch')
    print('-'*60)
    print('{:>2}{:>12}{:>15}{:>14}{:>16}{:>18}'.format('No','Home','Score','Away','Stadium','League'))
    for x in result :
        print('{:>1}{:>8}{:>16}{:>15}{:>11}{:>13}'.format(x[0],x[1],x[2],x[3],x[4],x[5]))

def editmatch():
    conn = sqlite3.connect(r'D:\kittiwarit_pythone\Project2.py\project2..db')
    c = conn.cursor()
    h = str(input('ใส่ชื่อทีมเหย้า :'))
    s = str(input('ใส่ผลคะเเนน :'))
    a = str(input('ใส่ชื่อทีมเยือน :'))
    st = str(input('ใส่ชื่อสนาม :'))
    l = str(input('ใส่ลีกการเเข่งขันฟุตบอล :'))
    c.execute('''UPDATE match SET Home=?,Score=?,Away=?,Stadium=?,League=?''',(h,s,a,st,l))
    conn.commit()
    print('เเก้ไขรายละเอียดทีมเรียบร้อยเเล้ว')
    conn.commit()

def deletedetailplayers():
    conn = sqlite3.connect(r'D:\kittiwarit_pythone\Project2.py\project2..db')
    c = conn.cursor()
    n = str(input('ลบนักเตะ :'))
    c.execute('''DELETE FROM name WHERE No = ?''',(n))
    conn.commit()
    print('ลบนักเตะสำเร็จเเล้ว')
    conn.close()
    
def indetailsplayers():
    conn = sqlite3.connect(r'D:\kittiwarit_pythone\Project2.py\project2..db')
    c = conn.cursor()
    n = str(input('เบอร์เสื้อนักเตะ :'))
    na = str(input('ชื่อนักเตะ :'))
    t = str(input('ทีมของนักเตะ :'))
    p = str(input('ตำเเหน่งการเล่นของนักเตะ :'))
    c.execute ('''INSERT INTO name(Number,Name,Team,Position)
    VALUES(?,?,?,?)'''
    ,(n,na,t,p))
    conn.commit()
    print('เพิ่มรายละเอียดนักเตะนักเตะสำเร็จเเล้ว')
    conn.close()

while True :
    menu_football()
    if choice == '1':
        inmatch()
    elif choice == '2':
        editmatch()
    elif choice == '3':
        indetailsplayers()
    elif choice == '4':
        deletedetailplayers()
    elif choice == '5':
        showplayers()
    elif choice == '6':
        showmatch()
    else :
        print('กรุณาเลือกรายการใหม่อีกครั้งครับ')
        continue