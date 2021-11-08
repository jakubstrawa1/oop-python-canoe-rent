# canoe rental project

import datetime as dt


class CanoeRental:

    def __init__(self, stock=0):
        self.stock = stock

    def displayStock(self):
        if self.stock < 5:
            print("We currently have only {} canoes available. Hurry up!".format(self.stock))
        else:
            print("We currently have {} canoes available to rent.".format(self.stock))
            return self.stock


    def rentCanoe(self, n):
    #Rents a canoe on a hourly basis
    #n means how many canoes do you want to rent 
        if n <= 0:
            print("The amount of canoes should be positive!")
            return None

        elif n > self.stock:
            print("Sorry, We currently have only {} canoes available".format(self.stock))
            return None

        else:
            now = dt.datetime.now()
            print("You have rented a {} canoe(s) on hourl basis today at {} hours.".format(n,now.hour))
            print("From now on, you will be charged 8$ for each hour per canoe.")
            print("I hope you enjoy your cruise and have fun!")

            self.stock -= n 
            return now

    def returnCanoe(self, request):
        rentalTime, rentalBasis, numOfCanoes = request 
        bill = 0
        if rentalTime and rentalBasis and numOfCanoes:
            self.stock += numOfCanoes
            now = dt.datetime.now()
            rentalPeriod = now - rentalTime

            if rentalBasis == 1:
                bill = round(rentalPeriod.seconds / 3600) * 8 * numOfCanoes

            if (2 <= numOfCanoes <= 5):
                print("You are eligible for Family Rental promotion of 30% discount")
                bill = bill * 0.7

            print ("Thank for returning your canoe.")
            print ("That will be ${}".format(bill))
            return bill
        else:
            print("Are you sure rented a canoe with our service?")
            return None 

class Customer:

    def __init__(self):
        self.bikes = 0
        self.rentalBasis = 0
        self.rentalTime = 0
        self.bill = 0

    def requestCanoe(self):
        canoes = input("How many canoes would you like to rent?")
        try:
            canoes = int(canoes)
        except ValueError:
            print("That's not a positive integer!")
            return -1
        else:
            self.canoes = canoes
        return self.canoes

    def returnCannoe(self):
        if self.rentalBasis and self.rentalTime and self.canoes:
            return self.rentalTime, self.rentalBasis, self.canoes
        else:
            return 0,0,0
        
