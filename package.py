class Package:
    def __init__(self, id, address, city, state, zip, delivery_deadline, weight, special_notes):
        '''
        Constructor for package object.
        '''
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.delivery_deadline = delivery_deadline
        self.weight = weight
        self.special_notes = special_notes
        self.status = 'HUB'
        self.time_delivered = None

    def __str__(self):
        '''
        Returns a string displaying all default package properties.
        '''
        return f'Address: {self.address + " " + self.city + ", " + self.state + " " + self.zip:<70} Deadline: {self.delivery_deadline:<12} Weight: {self.weight:<5} Special Notes: {self.special_notes}'