import sqlite3
conn = sqlite3.connect(r'D:\kittiwarit_pythone\Project\Project.db')
c = conn.cursor()
#c.execute('''CREATE TABLE football(NO integer PRIMARY KEY AUTOINCREMENT,
#    Match varchar(1000) NOT NULL,
#    Pname varchar(5000) NOT NULL,
#    Winrate varchar(1000) NOT NULL,
#    Channels varchar(1000) NOT NULL)''')
#conn.commit()
#conn.close()

def insert_football (Match,Pname,Winrate,Channels):
    try :
        conn = sqlite3.connect(r'D:\kittiwarit_pythone\Project\Project.db')
        c = conn.cursor()
        sql = '''  INSERT INTO football (Match,Pname,Winrate,Channels) VALUES (?,?,?,?) '''
        data = (Match,Pname,Winrate,Channels)
        c.execute(sql,data)
        conn.commit ()
        c.close ()
    except sqlite3.Error as e:
        print('Failed to insert : ',e)
    finally :
        if conn :
            conn.close ()

def menu() :
    global choice
    print('========== Football Club ==========')
    print('รายการเเข่งขันฟุตบอล [1]')
    print('รายชื่อนักฟุตบอล [2]')
    print('อัตราชนะ/Winrate [3]')
    print('ช่องทางการรับชม [4]')
    choice = input('กรุณาเลือกรายการที่ท่านต้องการค่ะ :')

def add_menu():
    global Match,Pname,Winrate,Channels
    Match = str('Liverpool              VS          Watford\n'
     'Chelsea                VS          Southamton\n'
     'Everton                VS          Arsenal\n'
     'Manchester City        VS          Manchester United\n'
     'Westham United         VS          Leeds United\n')
    Pname = str('Liverpool      VS       Watford\n'
    'No.1 Alisson               Vs        NO.26 Bachmann              GK\n'
    'No.4 V. van Dijk           Vs        No.27 C.Kabasele            CB\n'
    'No.12 J.Gomez              Vs        No.41 M.Barrett             CB\n'
    'No.26 A.Robertson          Vs        No.21 B.wilmot              LB\n'
    'No.66 T.Alexander-Arnold   Vs        No.11 A.Masina              RB\n'
    'No.3 Fabinho               Vs        No.12 K.Sema                CM\n'
    'No.14 J.Henderson          Vs        No.17 A.Lazaar              CM\n'
    'No.5 G.Wijnadum            Vs        No.19 W.Hughes              CM\n'
    'No.10 S.Mane               Vs        No.23 l.Sarr                LW\n'
    'No.9 R.Firmino             Vs        No.30 A.Gray                ST\n'
    'No.11 M.Salah              Vs        No.9  T.Deeney              RW\n' 
    'Coach : Jurrken Krop                 Coach : Gino Pozzo\n' #โค้ชทีม
    'Chelsea                  VS        Southamton\n' #รายชื่อนักเตะทีม เชลซี กับ เซาท์เเฮมตันป์
    'No.1Kepa Arrizabalaga      Vs        No.1 Alex McCarthy          GK\n'
    'No.2 Antonio Rüdiger       Vs        No.3Jack Stephens           CB\n'
    'No.3 Marcos Alonso         Vs        No.3Ryan Bertrand           CB\n'
    'No.4 Andres Chistensen     Vs        No.35. Jan Bednarek         CB\n'
    'No.15 Kurt Zouma           Vs        No.2 Kyle Walker-peters     CB\n'
    'NO.22 Hakim Ziyech         Vs        No.Oriol Romeu              CM\n'
    'No.5 Jorginho              Vs        No.8 Jame Ward-Prowse       CM\n'
    'No.7 N Golo Kante          Vs        No.17 Stuart Armstrong      CM\n'
    'NO.17 Mateo Kovacic        Vs        No.11 Nathan Redmond        CM\n'
    'No11. Timo                 Vs        No.9 Danny Ings             ST\n'
    'No.9 Tammy Abraham         Vs        No.10 Che Adam              ST\n'
    'Coach : Thomas Tuchel                Coach : Ralph Hasanhutti\n'
    'Everton      vs      Arsenal\n'
    'NO.1 Jordan Pickford        Vs      No.1 Bernd Leno              GK\n'
    'No.4 Mason Holgate          Vs      No.2 Hevtor Bellerin         CB\n'
    'No.5 Michael Keane          Vs      No.3 Kieran Tierney          CB\n'
    'No.12 Lucas Digne           Vs      No.16 Rob Holfing            CB\n'
    'No.8 Fabian Delph           Vs      No.25 Mohamed Elneny         CM\n'
    'No.21 Andre Gomes           Vs      No.32 Emile Smith Rowe       CM\n'
    'No.26 Tom Davies            Vs      No.34 Granit Xhaka           CM\n'
    'No.6 Allan                  Vs      No.7 Bukayo Saka             CM\n'
    'No.7 Richarlison            Vs      No.24 Reiss Nelson           ST\n'
    'No.17 Alex Iwobi            Vs      No.30 Eddie Nketiah          st\n'
    'No.20 Bernard               Vs      No.15 Waiilian               ST\n'
    'Manchester City        vs      Manchester United\n'
    'No.31 Ederson               Vs      No.1 David de gea            GK\n'
    'No.6 Nathan Ake             Vs      No.2 Victor Lindelof         CB\n'
    'No.2 Kyle Walker            Vs      No.3 Eric Bailly             Cb\n'
    'No.5 John Stones            Vs      No.Phil Jones                CB\n'
    'No.11 Oleksandr Zinchenko        vs      No.5 Harry Maguire      CB\n'
    'No.16 Rodrigo               Vs      No.6 Pual pogba              CM\n'
    'No.20 Bernardo Silva        Vs      No.18 Bruno Fernandes        CM\n'
    'No.25 Fernandinho           Vs      No.31 Nemanja Matic          CM\n'
    'No.21 Ferran Torres         Vs      No.34 Donny van de beek      ST\n'
    'No.7 Raheem Sterling        vs      No.Marcus Rashford           ST\n'
    'No.80 Cole Palmer           Vs      No.11 Mason Greenwood        ST\n'
    'No.10 Sergio Aguero         Vs      No.19. Amad Martial          ST\n'
    'Westham United       Vs      Leeds United\n'
    'No.1 Lukasz Fabibianski        Vs      No.13 Kiko Casilla       GK\n'
    'No.3 Aaron Cresswell     Vs      No.6 Liam Cooper               CB\n'
    'No.4 Fabian Balbuena     Vs      No.21 Pascal Struijk           CB\n'
    'No.21 Angelo Ogbonna     Vs      No.5 Roin Koch                 CB\n'
    'No.23 Issa Diop          Vs      No.35 Charlie Cresswell        CB\n'
    'No.10 Manuel Lanzini     Vs      No.4 Adam Forshaw              CM\n'
    'No.10 Mark Noble         Vs      No.10 Ezgjan Aliosko           CM\n'
    'No.18 Pablo Fornals      Vs      No.15 Stuart Dallas            CM\n'
    'No.41 Declan Rice        Vs      No.19 Pablo Hernandez          CM\n'
    'No.30 Michail Antonio    Vs      No.20 Rodrigo                  ST\n'
    'No.7 Andriy Yarmolenko   Vs      No.18 Raphinha                 ST\n'
    'No.20 Jarrod Bowen       Vs      No.17.Helder Costa             ST\n'
    'No.56 Emmanuel Longelo   Vs      No.52 Niall Huggins\n')
    Winrate = str('Liverpool                  VS          Watford  70 % - 30 %\n'
    'Chelsea                    Vs          Southamton 40 % - 60 %\n'
    'Everton                    VS          Arsenal 50 % - 50 %\n'
    'Manchester City            VS          Manchester United 60 % - 50 %\n' 
    'Westham United             VS          Leeds united 70 % - 30 %\n')
    Channels = str(' Liverpool VS Watford\n ''-------Channel-------\n'' Thairath tv,Amarin tv\n\n'
    'Chelsea VS Southamton\n ''-------Channel-------\n'' Voice tv,Workpoint tv\n\n'
    'Everton VS Arsenal\n ''-------Channel-------\n''       One 31\n\n'
    'Manchester City vs Manchester United\n ''-------Channel-------\n''       True id\n\n'
    'Westham United vs Leeds united\n ''-------Channel-------\n''       MONO 29\n\n' )

def Show():
    with sqlite3.connect(r'D:\kittiwarit_pythone\Project\Project.db') as con:
        con.row_factory = sqlite3.Row
        showmatch ="""SELECT * FROM football """
        for row in c.execute (showmatch):
            print(row[1])
def Show1():
    with sqlite3.connect(r'D:\kittiwarit_pythone\Project\Project.db') as con:
        con.row_factory = sqlite3.Row
        showmatch ="""SELECT * FROM football """
        for row in c.execute (showmatch):
            print(row[2])
def Show2():
    with sqlite3.connect(r'D:\kittiwarit_pythone\Project\Project.db') as con:
        con.row_factory = sqlite3.Row
        showmatch ="""SELECT * FROM football """
        for row in c.execute (showmatch):
            print(row[3])
def Show3():
    with sqlite3.connect(r'D:\kittiwarit_pythone\Project\Project.db') as con:
        con.row_factory = sqlite3.Row
        showmatch ="""SELECT * FROM football """
        for row in c.execute (showmatch):
            print(row[4])
add_menu()
insert_football (Match,Pname,Winrate,Channels)
while True:
    menu()
    if choice == '1':
        Show()
    elif choice == '2':
        Show1()
    elif choice == '3':
        Show2()
    elif choice == '4':
        Show3()