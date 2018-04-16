class Transaction:
    """Transaction class"""

    def __init__(self, location, pan, amount, email, first, last):
        self.location = location
        self.pan = pan
        self.amount = amount
        self.first = first
        self.last = last
        
    @property
    def pan(self):
        return '{}'.format(self.pan)

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def UpdateTransaction():
        return

    @property
    def FrequencyCheck():
        return

    @property
    def MathematicalFunction():
        return



    #@property
    #def amount(self):
        #return '{}'.format(self.amount)

    #@property
    #def location(self):
        #return '{}'.format(self.location)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def __repr__(self):
        return "Transaction('{}', '{}', {})".format(self.first, self.last, self.amount, self.location, self.pan)