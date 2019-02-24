"""Project Name: Hotel FrontDesk System
    Description: This is a console based simple hotel frontdesk system
    programmed in python.
    Written by:
      Hardikkumar Bhakta
"""

import time
from datetime import date, datetime, timedelta

class FrontDesk:
    def __init__(self, hotelName):
        self.hotelName = hotelName
        self.roomList = []

    def createRoom(self, n):
        i = 0
        while (i < n):
            print(" Creating Room...", i + 1)
            roomType = input("  What type of Room? (SB = Single Bed "
                             "or DB = Double Bed): ")
            r = Room(i + 100, roomType)
            r.makeVacant()
            self.addRoom(r)
            i += 1

    def addRoom(self, room):
        self.roomList.append(room)

    def removeRoom(self):
        self.roomList.remove(room)

    def searchRoom(self, rmNmbr):
        i = 0
        flag = False
        while (flag == False)&(i < len(self.roomList)):
            if (self.roomList[i].roomNumber == rmNmbr):
                flag = True
                room = self.roomList[i]
            i += 1
        return room

    def displayRoomList(self):
        if (len(self.roomList) == 0):
            print("\n Room List is empty!")
        else:
            i = 0
            print("\nList of Rooms",
                  "\n-----------------------------",
                  "\n Room#  Room Type    Status",
                  "\n-----------------------------")
            while (i < len(self.roomList)):
                print(" ",self.roomList[i].roomNumber,
                      " ", self.roomList[i].roomType,
                      " ", self.roomList[i].roomStatus)
                i += 1

class Room:
    roomTypes = {'SB': "Single Bed",
                 'DB': "Double Bed"}
    def __init__(self, roomNumber, aRoomType):
        self.roomNumber = roomNumber
        if (aRoomType not in Room.roomTypes):
            print("Invalid Room Type")
        else:
            self.roomType = Room.roomTypes[aRoomType]
            if (aRoomType.upper() == 'SB'):
                self.dailyRate = 60.00
                self.salesTax = 0.07
            elif (aRoomType.upper() == 'DB'):
                self.dailyRate = 70.00
                self.salesTax = 0.08
            
    def changeDailyRate(self, rate):
        self.dailyRate = rate
    def makeVacant(self):
        self.roomStatus = "Vacant"
    def makeOccupied(self):
        self.roomStatus = "Occupied"
    def isAvailable(self):
        if (self.roomStatus == "Vacant"):
            return True
        else:
            print("\n  This room is currently occupied."
                  "\n  Select vacant room.")
            return False
    def displayRoomRate(self):
        print("  Room and Rate Info:",
              "\n   Room Number: ", self.roomNumber,
              "\n   Room Type:   ", self.roomType,
              "\n   Daily Rate:  $%.2f" % self.dailyRate,
              "\n   Sales Tax:   %%%.2f" % self.salesTax, sep="")
        
class Guest:
    def __init__(self, lastName, firstName, gender, idNmbr, dob):
        self.lastName = lastName
        self.firstName = firstName
        self.guestName = firstName + " " + lastName
        self.gender = gender
        self.idNmbr = idNmbr
        self.dateOfBirth = dob
        
    def setAddressInfo(self, street, city, state, zipCode, country):
        self.street = street
        self.city = city
        self.state = state
        self.zipCode = zipCode
        self.country = country
        
    def setVehicleInfo(self, make, model, year, licensePlate):
        self.make = make
        self.model = model
        self.year = year
        self.licensePlate = licensePlate
        
    def displayGuestInfo(self):
        print("\n  Guest Name: ", self.guestName, "\n  ID Number:  ",
              self.idNmbr, "\n  DOB: ", self.dateOfBirth.strftime('%m/%d/%Y'), 
			  "\n  Address: \n  ", self.street, "\n  ", self.city, ",", 
			  self.state, self.zipCode, "\n  ", self.country,
              "\n  Vehicle Information:\n ", " Make: ", self.make,
              "\n   Model: ", self.model, "\n   Year: ",
              self.year,"\n   License Plate#: ", self.licensePlate)

class GuestStayReport:
    def __init__(self, numberOfDays, room):
        self.roomN = room
        self.roomNumber = room.roomNumber
        self.stayDays = numberOfDays
        self.checkInDate = date.today()
        self.checkOutDate = date.today() + timedelta(days = numberOfDays)
        self.rate = 0.00
        self.rentalCharge = 0.00
        self.tax = 0.00
        self.totalRent = 0.00
        self.amountDue = 0.00
        self.amountPaid = 0.00
        self.calculateAmountDue(self.stayDays)

    def addDays(self, nDays):
        self.stayDays += nDays
        self.checkOutDate += timedelta(days = nDays)
        self.calculateAmountDue(nDays)

    def deleteDays(self, nDays):
        if (nDays > self.stayDays):
            print("\n  Days Cannot be deleted! Check Guest Stay Info",
                  "\n  The guest is days of stay are less than the",
                  "\n  days you have entered.")
        else:
            self.stayDays -= nDays
            self.checkOutDate -= timedelta(days = nDays)
            self.rentalCharge -= self.roomN.dailyRate * nDays
            self.tax = self.roomN.salesTax * self.rentalCharge
            self.totalRent = self.rentalCharge + self.tax
            self.amountDue = self.rentalCharge + self.tax - self.amountPaid

    def calculateAmountDue(self, nDays):
        self.rentalCharge += self.roomN.dailyRate * nDays
        self.tax = self.roomN.salesTax * self.rentalCharge
        self.totalRent = self.rentalCharge + self.tax
        self.amountDue = self.rentalCharge + self.tax - self.amountPaid

    def addRentPaid(self, amount):
        self.amountPaid += amount
        self.amountDue -= amount

    def deleteRentPaid(self, amount):
        self.amountPaid -= amount
        self.amountDue += amount
        
    def displayGuestStayReport(self):
        print("\n  Room#:         ", self.roomNumber,
              "\n  Days of Stay:  ", self.stayDays,
              "\n  CheckIn Date:  ", self.checkInDate.strftime('%m/%d/%Y'),
              "\n  CheckOut Date: ", self.checkOutDate.strftime('%m/%d/%Y'),
              "\n  Rental Charge: $%.2f" % self.rentalCharge,
              "\n  Tax:           $%.2f" % self.tax,
              "\n  Total Rent:    $%.2f" % self.totalRent,
              "\n  Amount Due:    $%.2f" % self.amountDue,
              "\n  Amount Paid:   $%.2f" % self.amountPaid, sep="")
        
class GuestFolio:
    nextFolio = 10000
    def __init__(self, hotelName, guest, guestStayReport):
        self.hotelName = hotelName
        self.guest = guest
        self.guestStayReport = guestStayReport
        self.folioNumber = GuestFolio.nextFolio
        GuestFolio.nextFolio += 1
        
    def printGuestFolio(self, deskClerk):
        print("\n-------------------------------------------\n",
              self.hotelName, "\nFolio#: ", self.folioNumber,
              "\nDesk Clerk: ", deskClerk,
              "\n-------------------------------------------",
              "\nGuest Identification Information", sep="")
        self.guest.displayGuestInfo()
        print("\nGuest Stay and Rent Information")
        self.guestStayReport.displayGuestStayReport()
        print("\n-------------------------------------------",
              "\nGuest Signature ____________", " Date ________",
              "\n-------------------------------------------",
              sep="")

class GuestLog:
    def __init__(self):
        self.folioList = []
    def addGuestFolio(self, guestFolio):
        self.folioList.append(guestFolio)
    def removeGuestFolio(self, guestFolio):
        self.folioList.remove(guestFolio)
    def searchGuestFolio(self, folioNmbr):
        tempFolio = None
        if (len(self.folioList) == 0):
            print("\n Guest Log is Empty!")
        else:
            i = 0
            flag = False
            while (flag != True) & (i < len(self.folioList)):
                if (self.folioList[i].folioNumber == folioNmbr):
                    tempFolio = self.folioList[i]
                i += 1
        return tempFolio

    def editGuestFolio(self, guestFolio):
        option = 0
        while(option != 6):
            print("\n  *****************************",
                  "\n  *       Folio Menu          *",
                  "\n  *1. Display Guest Stay Info *",
                  "\n  *2. Add Days of Stay        *",
                  "\n  *3. Delete Days of Stay     *",
                  "\n  *4. Collect Rent Paid       *",
                  "\n  *5. Delete Rent Paid        *",
                  "\n  *6. Return to Main Menu     *",
                  "\n  *****************************",)
            option = int(input("  Enter your option: "))
            if (option == 1):
                guestFolio.guestStayReport.displayGuestStayReport()
            elif (option == 2):
                nDays = int(input("  How many more days "
                                  "do you want to add? "))
                guestFolio.guestStayReport.addDays(nDays)
            elif (option == 3):
                nDays = int(input("  How many days do you "
                                  "want to delete? "))
                guestFolio.guestStayReport.deleteDays(nDays)
            elif (option == 4):
                amount = float(input("  Enter Amount to Add: "))
                guestFolio.guestStayReport.addRentPaid(amount)
            elif (option == 5):
                amount = float(input("  Enter Amount to Delete: "))
                guestFolio.guestStayReport.deleteRentPaid(amount)
            elif (option == 6):
                print("\n  Returning to Main Menu...")
            else:
                print("\n  WRONG OPTION!")

    def displayGuestLedger(self):
        if (len(self.folioList) == 0):
            print("Guest Ledger is empty!")
        else:
            print("\nDisplaying Guest Ledger:\n",
                  '%6s'%"Folio#",'  %-21s'%"Guest Name",
                  ' %-12s'%"CheckInDate",' %-12s'%"CheckOutDate",
                  ' %-10s'%"AmountPaid", ' %-10s'%"AmountDue")
            i = 0
            while (i < len(self.folioList)):
                print("%6s"% self.folioList[i].folioNumber,
                      "  %-21s"% self.folioList[i].guest.guestName,
                      "  %-11s"% self.folioList[i].guestStayReport.checkInDate.strftime("%m/%d/%Y"),
                      "  %-11s"% self.folioList[i].guestStayReport.checkOutDate.strftime("%m/%d/%Y"),
                      " $%-11.2f" % self.folioList[i].guestStayReport.amountPaid,
                      " $%-11.2f" % self.folioList[i].guestStayReport.amountDue)
                i += 1

class GuestRegistrar:
    def __init__(self, deskClerk):
        self.deskClerk = deskClerk

    def rentRoom(self, hotelName, room):    
        room.displayRoomRate() #Displaying Room and Rate Info
        print("\n Enter Guest Information:")
        lastN = input("  Last Name: ")
        firstN = input("  First Name: ")
        gender = input("  Gender: ")
        idNmbr = input("  ID/DL Number: ")
        dob = datetime.strptime(input("  Date of Birth (m/d/y): "), '%m/%d/%Y')
        
        print("\n Guest's Address:")
        street = input("  Street: ")
        city = input("  City: ")
        state = input("  State: ")
        zipCode = input("  Zip Code: ")
        country = input("  Country: ")

        print("\n Guest's Vehicle Information:")
        make = input("  Make: ")
        model = input("  Model: ")
        year = input("  Year: ")
        licensePlate = input("  License Plate#: ")

        guest = Guest(lastN, firstN, gender, idNmbr, dob)
        guest.setAddressInfo(street, city, state, zipCode, country)
        guest.setVehicleInfo(make, model, year, licensePlate)
        
        print("\n Guest Stay Information")
        numberOfDays = int(input("  How many days the guest want to stay? "))
        
        guestStayReport = GuestStayReport(numberOfDays, room)
        guestStayReport.displayGuestStayReport()

        amount = float(input("  Enter Amount Paid: "))
        
        guestStayReport.addRentPaid(amount)
        guestStayReport.displayGuestStayReport()
        room.makeOccupied()
        
        guestFolio = GuestFolio(hotelName, guest, guestStayReport)

        return guestFolio
    
#1.---------------------------------------
hotelName = input("Enter Name of Hotel: ")
frontDesk = FrontDesk(hotelName)

numberOfRooms = int(input("How many rooms do you want to create? "))
frontDesk.createRoom(numberOfRooms)
frontDesk.displayRoomList()

#2.---------------------------------------
guestLog = GuestLog()
option = 0
while (option != 6):
    print("\n*****************************",
          "\n*       Main Menu           *",
          "\n*1. Rent New Room           *",
          "\n*2. View Room List & Status *",
          "\n*3. View GuestLedger        *",
          "\n*4. Edit Guest Folio        *",
          "\n*5. Print Guest Folio       *",
          "\n*6. Quit                    *",
          "\n*****************************")
    option = int(input("Enter your option: "))

    if (option == 1):
        deskClerkName = input(" Desk Clerk Name: ")
        guestRegistrar = GuestRegistrar(deskClerkName)
        roomNumber = int(input("\n Which Room Number do you want to rent? "))
        room = frontDesk.searchRoom(roomNumber)
        if (room.isAvailable() == True):
            guestFolio = guestRegistrar.rentRoom(hotelName, room)
            guestLog.addGuestFolio(guestFolio)
            opt = input(" Do you want to print this guest folio? (Yes=Y/No=N) ")
            if (opt.upper() == "Y"):
                guestFolio.printGuestFolio(deskClerkName)
    elif (option == 2):
        frontDesk.displayRoomList()
    elif (option == 3):
        guestLog.displayGuestLedger()
    elif (option == 4):
        folioNumber = int(input(" Enter Folio#: "))
        guestFolio = guestLog.searchGuestFolio(folioNumber)
        guestLog.editGuestFolio(guestFolio)
    elif (option == 5):
        folioNumber = int(input(" Enter Folio#: "))
        guestFolio = guestLog.searchGuestFolio(folioNumber)
        guestFolio.printGuestFolio(deskClerkName)
    elif (option == 6):
        print("You have exited the program!")
    else:
        print("WRONG OPTION!")

