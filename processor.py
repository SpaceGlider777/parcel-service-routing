import csv
import globals
import os.path

from package import Package
from hashtable import HashTable

path = os.path.abspath(os.path.dirname(__file__))

def load_package_data():
    '''
    Space: O(n)
    Time: O(n)
    Loads the package data into a hash table.
    '''
    with open(os.path.join(path, 'csv/WGUPS Package File.csv'), 'r', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        data = list(reader)
        globals.packages = HashTable(len(data))
        for row in data:
            package = Package(int(row[0]), row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            globals.packages.insert(package.id, package)

def load_address_data():
    '''
    Space: O(n)
    Time: O(n)
    Loads the address data into a list.
    '''
    with open(os.path.join(path, 'csv/WGUPS Distance Table.csv'), 'r', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            globals.addresses.append(row[0].strip().replace('\n', ' '))

def load_distance_data():
    '''
    Space: O(n²)
    Time: O(n²)
    Loads the distance data into a N by N matrix.
    '''
    with open(os.path.join(path, 'csv/WGUPS Distance Table.csv'), 'r', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            globals.distances.append([])
            globals.distances[-1].extend(row[1:])

        # Replicate values for empty strings
        for i in range(len(globals.distances)):
            for j in range(len(globals.distances)):
                if globals.distances[i][j] == '':
                    globals.distances[i][j] = globals.distances[j][i]

        # Convert to float
        for i in range(len(globals.distances)):
            for j in range(len(globals.distances)):
                    globals.distances[i][j] = float(globals.distances[i][j])
