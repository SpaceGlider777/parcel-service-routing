import datetime

from utils import get_nearest_neighbor, get_distance

class Truck:
    def __init__(self):
        '''
        Constructor for truck object.
        '''
        self.packages = []
        self.packages_delivered = []
        self.max_packages = 16
        self.speed = 18
        self.location = 'HUB'
        self.miles = 0
        self.mile_history = [0]
        self.time = datetime.datetime(2023, 1, 1, hour=8, minute=0, second=0)

    def add_package(self, package):
        '''
        Space: O(1)
        Time: O(1)
        Adds a package to the truck.
        Raises IndexError if truck is already full.
        '''
        if len(self.packages) == self.max_packages:
            raise IndexError('Truck is full.')
        self.packages.append(package)

    def remove_package(self, package):
        '''
        Space: O(1)
        Time: O(n)
        Removes a package from the truck if it exists.
        '''
        if package in self.packages:
            self.packages.remove(package)

    def deliver_package(self):
        '''
        Space: O(1)
        Time: O(n)
        Utilizes the nearest neighbor function to deliver a package.
        Updates the truck time, miles, mile history, location, package status, package deilvery time.
        Adds package to the package delivered list and removes it from packages list.
        '''
        min_index, miles  = get_nearest_neighbor(self.location, self.packages)
        self.time += datetime.timedelta(hours=float(miles / self.speed))
        self.miles += miles
        self.mile_history.append(self.miles)
        self.location = self.packages[min_index].address + f' ({self.packages[min_index].zip})'
        self.packages[min_index].status = 'DELIVERED'
        self.packages[min_index].time_delivered = self.time
        self.packages_delivered.append(self.packages[min_index])
        self.packages.remove(self.packages[min_index])

    def deliver_all_packages(self):
        '''
        Space: O(1)
        Time: O(n²)
        Delivers all packages.
        '''
        while (len(self.packages) > 0):
            self.deliver_package()

    def return_to_hub(self):
        '''
        Returns the truck to the HUB.
        Updates truck time, miles, miles history, and location.
        '''
        miles = get_distance(self.location, 'HUB')
        self.time += datetime.timedelta(hours=float(miles / self.speed))
        self.miles += miles
        self.mile_history.append(self.miles)
        self.location = 'HUB'
