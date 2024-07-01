from pickle import load, dump
import time
import random
import os

#_______________________CLASS TICKETS_________________
class Tickets:
    def __init__(self):
        self.no_ofac1stclass = 0
        self.totaf = 0
        self.no_ofac2ndclass = 0
        self.no_ofac3rdclass = 0
        self.no_ofsleeper = 0
        self.no_oftickets = 0
        self.name = ''
        self.age = 0
        self.resno = 0
        self.status = ''

    #__________RETURNS RESERVATION NUMBER___________
    def ret(self):
        return self.resno

    #___________RETURNS NAME_____________
    def retname(self):
        return self.name

    #_________________DISPLAYS THE DATA_______________
    def display(self):
        f = 0
        try:
            with open("tickets.dat", "rb") as fin1:
                n = int(input("ENTER PNR NUMBER: "))
                print("\n\nFETCHING DATA . . .".center(80))
                time.sleep(1)
                print('PLEASE WAIT...!!'.center(80))
                time.sleep(1)
                os.system('cls')
                while True:
                    try:
                        tick = load(fin1)
                        if n == tick.ret():
                            f = 1
                            print("=" * 80)
                            print("PNR STATUS".center(80))
                            print("=" * 80)
                            print("\nPASSENGER'S NAME:", tick.name)
                            print("\nPASSENGER'S AGE:", tick.age)
                            print("\nPNR NO:", tick.resno)
                            print("\nSTATUS:", tick.status)
                            print("\nNO OF SEATS BOOKED:", tick.no_oftickets)
                            print("=" * 80)
                    except EOFError:
                        break
        except FileNotFoundError:
            print("ERROR: tickets.dat file not found.")
        if f == 0:
            print("WRONG PNR NUMBER..!!")
    
    def pending(self):
        self.status = "WAITING LIST"
        print("PNR NUMBER:", self.resno)
        time.sleep(1.2)
        print("STATUS:", self.status)
        print("NO OF SEATS BOOKED:", self.no_oftickets)

    def confirmation(self):
        self.status = "CONFIRMED"
        print("PNR NUMBER:", self.resno)
        time.sleep(1.5)
        print("STATUS:", self.status)

    def cancellation(self):
        r = int(input("ENTER PNR NUMBER: "))
        found = False
        try:
            with open("tickets.dat", "rb") as fin, open("temp.dat", "wb") as fout:
                while True:
                    try:
                        tick = load(fin)
                        if tick.ret() != r:
                            dump(tick, fout)
                        else:
                            found = True
                    except EOFError:
                        break
        except FileNotFoundError:
            print("ERROR: tickets.dat file not found.")
        os.remove("tickets.dat")
        os.rename("temp.dat", "tickets.dat")
        if not found:
            print("NO SUCH RESERVATION NUMBER FOUND")
        else:
            print("TICKET CANCELLED")

    #__________________RESERVES THE TICKET_______________
    def reservation(self):
        trainno = int(input("ENTER THE TRAIN NO: "))
        found = False
        try:
            with open("trdetails.dat", "rb") as fin2:
                while True:
                    try:
                        tr = load(fin2)
                        if trainno == tr.gettrainno():
                            print("\nTRAIN NAME IS:", tr.gettrainname())
                            found = True
                            print("-" * 80)
                            no_ofac1st = tr.getno_ofac1stclass()
                            no_ofac2nd = tr.getno_ofac2ndclass()
                            no_ofac3rd = tr.getno_ofac3rdclass()
                            no_ofsleeper = tr.getno_ofsleeper()
                            with open("tickets.dat", "ab") as fout1:
                                self.name = input("ENTER THE PASSENGER'S NAME: ")
                                self.age = int(input("PASSENGER'S AGE: "))
                                print("\t\t SELECT A CLASS YOU WOULD LIKE TO TRAVEL IN :-")
                                print("1. AC FIRST CLASS")
                                print("2. AC SECOND CLASS")
                                print("3. AC THIRD CLASS")
                                print("4. SLEEPER CLASS")
                                c = int(input("\t\t\tENTER YOUR CHOICE = "))
                                os.system('cls')
                                amt1 = 0
                                if c == 1:
                                    self.no_oftickets = int(input("ENTER NO_OF FIRST CLASS AC SEATS TO BE BOOKED: "))
                                    amt1 = 1000 * self.no_oftickets
                                    self.resno = random.randint(1000, 2546)
                                    x = no_ofac1st - self.no_oftickets
                                elif c == 2:
                                    self.no_oftickets = int(input("ENTER NO_OF SECOND CLASS AC SEATS TO BE BOOKED: "))
                                    amt1 = 900 * self.no_oftickets
                                    self.resno = random.randint(1000, 2546)
                                    x = no_ofac2nd - self.no_oftickets
                                elif c == 3:
                                    self.no_oftickets = int(input("ENTER NO_OF THIRD CLASS AC SEATS TO BE BOOKED: "))
                                    amt1 = 800 * self.no_oftickets
                                    self.resno = random.randint(1000, 2546)
                                    x = no_ofac3rd - self.no_oftickets
                                elif c == 4:
                                    self.no_oftickets = int(input("ENTER NO_OF SLEEPER CLASS SEATS TO BE BOOKED: "))
                                    amt1 = 550 * self.no_oftickets
                                    self.resno = random.randint(1000, 2546)
                                    x = no_ofsleeper - self.no_oftickets
                                else:
                                    print("INVALID CHOICE")
                                    return
                                print("TOTAL AMOUNT TO BE PAID =", amt1)
                                print("PROCESSING. .", end='', flush=True)
                                time.sleep(0.5)
                                print(".", end='', flush=True)
                                time.sleep(0.3)
                                print('.', end='', flush=True)
                                time.sleep(2)
                                os.system('cls')
                                if x > 0:
                                    self.confirmation()
                                    dump(self, fout1)
                                else:
                                    self.pending()
                                    dump(self, fout1)
                            break
                    except EOFError:
                        break
        except FileNotFoundError:
            print("ERROR: trdetails.dat file not found.")
        if not found:
            print("\n\n\n\n\n\n\t\t\t\tNO SUCH TRAINS FOUND !!")

#____________________CLASS TRAIN__________________
class Train:
    def __init__(self):
        self.trainno = 0
        self.no_ofac1stclass = 0
        self.no_ofac2ndclass = 0
        self.no_ofac3rdclass = 0
        self.no_ofsleeper = 0
        self.trainname = ''
        self.startingpt = ''
        self.destination = ''

    #_______________________GETS INPUT__________________
    def getinput(self):
        print("=" * 80)
        print("\t\t\t  ENTER THE TRAIN DETAILS")
        print("=" * 80)
        self.trainname = input("ENTER THE TRAIN NAME: ").upper()
        self.trainno = int(input("ENTER THE TRAIN NUMBER: "))
        self.no_ofac1stclass = int(input("ENTER NO_OF AC FIRST CLASS SEATS TO BE RESERVED: "))
        self.no_ofac2ndclass = int(input("ENTER NO_OF AC SECOND CLASS SEATS TO BE RESERVED: "))
        self.no_ofac3rdclass = int(input("ENTER NO_OF AC THIRD CLASS SEATS TO BE RESERVED: "))
        self.no_ofsleeper = int(input("ENTER NO_OF SLEEPER CLASS SEATS TO BE RESERVED: "))
        self.startingpt = input("ENTER THE STARTING POINT: ")
        self.destination = input("ENTER THE DESTINATION POINT: ")
        os.system('cls')

    #___________________DISPLAYS DATA_________________
    def output(self):
        print("=" * 80)
        print("THE ENTERED TRAIN NAME IS:", self.trainname)
        print("THE TRAIN NUMBER IS:", self.trainno)
        print("STARTING POINT ENTERED IS:", self.startingpt)
        print("DESTINATION POINT ENTERED IS:", self.destination)
        print("NO_OF AC FIRST CLASS SEATS RESERVED ARE:", self.no_ofac1stclass)
        print("NO_OF AC SECOND CLASS SEATS RESERVED ARE:", self.no_ofac2ndclass)
        print("NO_OF AC THIRD CLASS SEATS RESERVED ARE:", self.no_ofac3rdclass)
        print("NO_OF SLEEPER CLASS SEATS RESERVED ARE:", self.no_ofsleeper)
        print("=" * 80)

    #_______RETURNS TRAIN NAME, NUMBER, CLASS, STARTING PT., DESTINATION____________
    def gettrainname(self):
        return self.trainname

    def gettrainno(self):
        return self.trainno

    def getno_ofac1stclass(self):
        return self.no_ofac1stclass

    def getno_ofac2ndclass(self):
        return self.no_ofac2ndclass

    def getno_ofac3rdclass(self):
        return self.no_ofac3rdclass

    def getno_ofsleeper(self):
        return self.no_ofsleeper

    def getstartingpt(self):
        return self.startingpt

    def getdestination(self):
        return self.destination

#___________________WRITES THE DATA__________________
def writedata():
    with open("trdetails.dat", "ab") as fout:
        t = Train()
        t.getinput()
        dump(t, fout)
        print("DATA RECORDED IN THE DATABASE..!!")

#__________________DISPLAYS THE DATA__________________
def displaydata():
    try:
        with open("trdetails.dat", "rb") as fin:
            while True:
                try:
                    t = load(fin)
                    t.output()
                except EOFError:
                    break
    except FileNotFoundError:
        print("ERROR: trdetails.dat file not found.")

#__________________DELETES THE DATA__________________
def deletedata():
    r = int(input("ENTER THE TRAIN NUMBER TO BE DELETED: "))
    found = False
    try:
        with open("trdetails.dat", "rb") as fin, open("temp.dat", "wb") as fout:
            while True:
                try:
                    t = load(fin)
                    if t.gettrainno() != r:
                        dump(t, fout)
                    else:
                        found = True
                except EOFError:
                    break
    except FileNotFoundError:
        print("ERROR: trdetails.dat file not found.")
    os.remove("trdetails.dat")
    os.rename("temp.dat", "trdetails.dat")
    if not found:
        print("NO SUCH TRAINS FOUND..!!")
    else:
        print("TRAIN RECORD DELETED")

#_____________________MAIN MENU__________________
def main_menu():
    while True:
        print("****************************** RAILWAY RESERVATION SYSTEM *******************************")
        print("1. RESERVE A TICKET")
        print("2. ENQUIRE A TICKET")
        print("3. CANCEL A TICKET")
        print("4. CREATE A NEW TRAIN RECORD")
        print("5. DISPLAY TRAIN RECORDS")
        print("6. DELETE A TRAIN RECORD")
        print("0. EXIT")
        choice = int(input("ENTER YOUR CHOICE: "))
        os.system('cls')
        if choice == 1:
            t = Tickets()
            t.reservation()
        elif choice == 2:
            t = Tickets()
            t.display()
        elif choice == 3:
            t = Tickets()
            t.cancellation()
        elif choice == 4:
            writedata()
        elif choice == 5:
            displaydata()
        elif choice == 6:
            deletedata()
        elif choice == 0:
            print("THANK YOU FOR USING THE RAILWAY RESERVATION SYSTEM. GOODBYE!")
            break
        else:
            print("INVALID CHOICE. PLEASE TRY AGAIN.")
            time.sleep(2)
            os.system('cls')

if __name__ == "__main__":
    main_menu()