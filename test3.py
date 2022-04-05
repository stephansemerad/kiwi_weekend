import csv

from numpy import place
import os

os.system('cls')


class Flight():
    def __init__(self, data):
        self.start = data['origin']
        self.end = data['destination']

    def __repr__(self):
        return f'{self.start} > {self.end}'


csv_file = open('./examples/example0.csv')
csv_read = csv.DictReader(csv_file, delimiter=',')
data = [Flight(x) for x in csv_read]


start = 'ECV'
end = 'RFZ'
path = []

starting_points = [x for x in data if x.start == start]


def get_flights(start='WIW', end='ECV', options=[], ignore=[]):

    for flight in data:
        if flight.start == start and flight.end == end:
            options.append([flight])
        else:
            if flight.start == start and flight.end not in ignore:
                print('possibility to fly to', flight.end)

    return options


print('start', 'ECV')
print('end: ', 'WIW')
start = 'ECV'
end = 'WIW'
options = []
ignore = [start]

results = get_flights(start, end, options, ignore)

# results = []
# for flight in starting_points:
#     connection = get_flights(start, end, flight, data)
#     results.append(connection)

print(results)
