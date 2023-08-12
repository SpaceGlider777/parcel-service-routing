import datetime

# Holds all packages in hash table
packages = None

# Holds all addresses in array
addresses = []

# Holds all distances in N by N array
distances = []

# Sets the current time to 8:00 AM
cur_time = datetime.datetime(2023, 1, 1, hour=8, minute=0, second=0).time()