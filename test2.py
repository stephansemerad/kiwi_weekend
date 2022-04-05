# Approach with nodes and edges. This


from multiprocessing import connection
import sys
import csv
import json
import argparse


class Flight():
    def __init__(self, data):
        self.flight_no = data['flight_no']
        self.origin = data['origin']
        self.destination = data['destination']

        self.start = data['origin']
        self.end = data['destination']

        self.departure = data['departure']
        self.arrival = data['arrival']

    def __repr__(self):
        return f'{self.origin} > {self.destination}'


csv_file = open('./examples/example0.csv')
csv_read = csv.DictReader(csv_file, delimiter=',')
data = [Flight(x) for x in csv_read]

nodes = []
edges = []
for flight in data:
    if flight.origin not in nodes:
        nodes.append(flight.origin)
    if flight.destination not in nodes:
        nodes.append(flight.destination)
    edges.append(flight)


def get_children(start):
    print('get_children')
    children = []
    for i in edges:
        if i.start == start and i.end != start:
            children.append(i)
    return children


results = []
children = get_children('ECV')
for child in children:
    print('child', child)
    if child.end == 'WIW':
        results.append(child)


# results = []
# # Step 1 - Get Children
# children = get_children('ECV')
# for child in children:
#     print('child', child)
#     if child.end == 'WIW':
#         results.append(child)
#     else:
#         gathering = []
#         gathering.append(child)
#         # get child of child
#         children2 = get_children(child.end)
#         for child2 in children2:
#             print('child2: ', child2)
#             if child2.end == 'WIW':
#                 gathering.append(child2)
