import sys
import datetime
import globals

def get_distance(address1, address2):
    '''
    Space: O(1)
    Time: O(n)
    Gets distance between two addresses using distance matrix.
    '''
    index1 = globals.addresses.index(address1)
    index2 = globals.addresses.index(address2)
    return globals.distances[index1][index2]

def get_nearest_neighbor(address, packages):
    '''
    Space: O(1)
    Time: O(n)
    Gets the nearest neighbor from packages to the given address.
    '''
    min_neighbor_index = 0
    min_dist = sys.maxsize
    for i in range(len(packages)):
        cur_dist = get_distance(address, packages[i].address + f' ({packages[i].zip})')
        if cur_dist < min_dist:
            min_neighbor_index = i
            min_dist = cur_dist

    return min_neighbor_index, min_dist

def load_packages(truck, package_id_list):
    '''
    Space: O(1)
    Time: O(n)
    Loads packages onto a truck given a list of package IDs.
    '''
    for id in package_id_list:
        truck.add_package(globals.packages.get(id))

def print_package_statuses(truck1, truck2, truck3):
    '''
    Space: O(n)
    Time: O(nlog(n))
    Prints all package statuses.
    '''
    # Copy packages into list and sort by package ID
    packages_list = []
    for bucket in globals.packages.table:
        for package in bucket:
            packages_list.append(package)
    packages_list.sort(key=lambda i: i.id)

    # Compare delivery time to current time to get package status
    for package in packages_list:
        if package in truck1.packages_delivered or package in truck1.packages:
            if globals.cur_time <= datetime.time(hour=8, minute=0, second=0):
                print(f'{"Package " + str(package.id) + " - Status: HUB":<45}', end=' ')
            elif package.time_delivered is not None and package.time_delivered.time() <= globals.cur_time:
                print(f'{"Package " + str(package.id) + " - Status: " + package.status + " at " + str(package.time_delivered.time()):<45}', end=' ')
            else:
                print(f'{"Package " + str(package.id) + " - Status: EN ROUTE":<45}', end=' ')
        elif package in truck2.packages_delivered or package in truck2.packages:
            if globals.cur_time <= datetime.time(hour=9, minute=5, second=0):
                print(f'{"Package " + str(package.id) + " - Status: HUB":<45}', end=' ')
            elif package.time_delivered is not None and package.time_delivered.time() <= globals.cur_time:
                print(f'{"Package " + str(package.id) + " - Status: " + package.status + " at " + str(package.time_delivered.time()):<45}', end=' ')
            else:
                print(f'{"Package " + str(package.id) + " - Status: EN ROUTE":<45}', end=' ')
            
        elif package in truck3.packages_delivered or package in truck3.packages:
            if globals.cur_time <= min(truck1.time, truck2.time).time():
                print(f'{"Package " + str(package.id) + " - Status: HUB":<45}', end=' ')
            elif package.time_delivered is not None and package.time_delivered.time() <= globals.cur_time:
                print(f'{"Package " + str(package.id) + " - Status: " + package.status + " at " + str(package.time_delivered.time()):<45}', end=' ')
            else:
                print(f'{"Package " + str(package.id) + " - Status: EN ROUTE":<45}', end=' ')
        
        # Print package details
        print(package)

def print_package_status(id, truck1, truck2, truck3):
    '''
    Space: O(1)
    Time: O(1)
    Prints a single package given package ID.
    '''
    # Get package from hash table
    package = globals.packages.get(id)

    # If package is None print error message
    if package is None:
        print('Package not found')
        return

    # Check which truck the package is in to print the status
    if package in truck1.packages_delivered or package in truck1.packages:
        if globals.cur_time <= datetime.time(hour=8, minute=0, second=0):
            print(f'{"Package " + str(package.id) + " - Status: HUB":<45}', end=' ')
        elif package.time_delivered is not None and package.time_delivered.time() <= globals.cur_time:
            print(f'{"Package " + str(package.id) + " - Status: " + package.status + " at " + str(package.time_delivered.time()):<45}', end=' ')
        else:
            print(f'{"Package " + str(package.id) + " - Status: EN ROUTE":<45}', end=' ')
    elif package in truck2.packages_delivered or package in truck2.packages:
        if globals.cur_time <= datetime.time(hour=9, minute=5, second=0):
            print(f'{"Package " + str(package.id) + " - Status: HUB":<45}', end=' ')
        elif package.time_delivered is not None and package.time_delivered.time() <= globals.cur_time:
            print(f'{"Package " + str(package.id) + " - Status: " + package.status + " at " + str(package.time_delivered.time()):<45}', end=' ')
        else:
            print(f'{"Package " + str(package.id) + " - Status: EN ROUTE":<45}', end=' ')
        
    elif package in truck3.packages_delivered or package in truck3.packages:
        if globals.cur_time <= min(truck1.time, truck2.time).time():
            print(f'{"Package " + str(package.id) + " - Status: HUB":<45}', end=' ')
        elif package.time_delivered is not None and package.time_delivered.time() <= globals.cur_time:
            print(f'{"Package " + str(package.id) + " - Status: " + package.status + " at " + str(package.time_delivered.time()):<45}', end=' ')
        else:
            print(f'{"Package " + str(package.id) + " - Status: EN ROUTE":<45}', end=' ')
    
    # Print package details
    print(package)

def print_mileage(truck1, truck2, truck3):
    '''
    Prints all truck mileages.
    Gets each trucks mileage by searching through truck object's mile_history property.
    '''
    truck1_mile_history_index = 0
    truck2_mile_history_index = 0
    truck3_mile_history_index = 0

    # Get miles for delivering packages
    for bucket in globals.packages.table:
        # Increments truck mile history indexes if a package was delivered
        for package in bucket:
            if package in truck1.packages_delivered or package in truck1.packages:
                if package.time_delivered is not None and package.time_delivered.time() <= globals.cur_time:
                    truck1_mile_history_index += 1
            elif package in truck2.packages_delivered or package in truck2.packages:
                if package.time_delivered is not None and package.time_delivered.time() <= globals.cur_time:
                    truck2_mile_history_index += 1
            elif package in truck3.packages_delivered or package in truck3.packages:
                if package.time_delivered is not None and package.time_delivered.time() <= globals.cur_time:
                    truck3_mile_history_index += 1

    # Increment truck mile history index if truck returned to hub
    if truck1.time.time() <= globals.cur_time:
        truck1_mile_history_index += 1
    
    if truck2.time.time() <= globals.cur_time:
        truck2_mile_history_index += 1

    if truck3.time.time() <= globals.cur_time:
        truck3_mile_history_index += 1
    
    print(f'Truck 1: {truck1.mile_history[truck1_mile_history_index]:.1f} miles')
    print(f'Truck 2: {truck2.mile_history[truck2_mile_history_index]:.1f} miles')
    print(f'Truck 3: {truck3.mile_history[truck3_mile_history_index]:.1f} miles')
    print(f'Total: {truck1.mile_history[truck1_mile_history_index] + truck2.mile_history[truck2_mile_history_index] + truck3.mile_history[truck3_mile_history_index]:.1f} miles')
