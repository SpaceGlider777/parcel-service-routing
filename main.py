import datetime
import sys
import globals

from processor import load_package_data, load_address_data, load_distance_data
from utils import load_packages, print_package_statuses, print_package_status, print_mileage
from truck import Truck

if __name__ == '__main__':
    # Load packages into hash table
    load_package_data()

    # Load address data into list
    load_address_data()

    # Load distance data into matrix
    load_distance_data()

    # Create three trucks
    truck1 = Truck()
    truck2 = Truck()
    # Set truck 2 time to 9:05 AM
    truck2.time = datetime.datetime(2023, 1, 1, hour=9, minute=5, second=0)
    truck3 = Truck()

    # Loads all packages with a deadline and without delay
    # Leaves at 8:00 AM
    load_packages(truck1, [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40, 2, 4, 5])
    truck1.deliver_all_packages()
    truck1.return_to_hub()

    # Loads all packages with a deadline and with delay
    # Leaves at 9:05 AM
    load_packages(truck2, [3, 6, 18, 28, 32, 36, 38, 7, 8, 9, 10, 11, 12, 17, 21])
    truck2.deliver_all_packages()
    truck2.return_to_hub()

    # Loads the rest of the packages
    # Leaves when a driver is available
    truck3.time = min(truck1.time, truck2.time)
    load_packages(truck3, [22, 23, 24, 25, 26, 27, 33, 35, 39])
    truck3.deliver_all_packages()
    truck3.return_to_hub()

    # User options
    while True:
        try:
            print()
            print(f'Time: {globals.cur_time}')
            print('1. Set time')
            print('2. Delivery statuses')
            print('3. Single package delivery status')
            print('4. Truck mileages')
            print('5. Exit\n')
            choice = int(input('Enter a choice (1-5): '))
            print()

            if choice == 1:
                # Set a new time
                new_time = input('Enter a time: ')
                globals.cur_time = datetime.datetime.strptime(new_time, '%H:%M').time()
            elif choice == 2:
                # Print all package statuses
                print_package_statuses(truck1, truck2, truck3)
            elif choice == 3:
                # Print a single package status
                id = int(input('Enter package ID: '))
                print_package_status(id, truck1, truck2, truck3)
            elif choice == 4:
                # Print truck mileages
                print_mileage(truck1, truck2, truck3)
            elif choice == 5:
                # Exit program
                sys.exit()
            else:
                raise ValueError('Invalid choice')
        except ValueError as e:
            print(f'{e}\n')
