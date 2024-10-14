
class BookingLibs():

    def __init__(self, bookingid=0, pickupaddress=None, date=None, time=None,dropofaddress=None, bookingstatus=None,
                 cid=None, did=None):

        self.bookingid=bookingid
        self.pickupaddress=pickupaddress
        self.date=date
        self.time=time
        self.dropofaddress=dropofaddress
        self.bookingstatus=bookingstatus
        self.cid=cid
        self.did=did

    #Getter
    def getBookingid(self):
        return self.bookingid

    def getPickupaddress(self):
        return self.pickupaddress

    def getDate(self):
        return self.date

    def getTime(self):
        return self.time

    def getDropofaddress(self):
        return self.dropofaddress

    def getBookingstatus(self):
        return self.bookingstatus

    def getCid(self):
        return self.cid

    def getDid(self):
        return self.did

    def setBookingid(self, bookingid):
        self.bookingid=bookingid

    def setPickupaddress(self, pickupaddress):
        self.pickupaddress=pickupaddress

    def setDate(self, date):
        self.date=date

    def setTime(self, time):
        self.time=time

    def setDropoffaddress(self, dropofaddress):
        self.dropofaddress=dropofaddress

    def setBookingstatus(self, bookingstatus):
        self.bookingstatus=bookingstatus

    def setCid(self, cid):
        self.cid=cid

    def setDid(self, did):
        self.did=did

    def __str__(self):
        return ('{},{},{},{},{},{},{},{}'.format(self.bookingstatus, self.pickupaddress, self.date, self.time, self.dropofaddress, self.bookingstatus, self.cid, self.did))