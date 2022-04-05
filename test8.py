import pprint
from collections import defaultdict
import csv
import os
from datetime import datetime
os.system('cls')


class Flight:
    def __init__(self, id, data):
        self.id = id
        self.start = data['origin']
        self.end = data['destination']
        self.departure = datetime. strptime(
            data['departure'], '%Y-%m-%dT%H:%M:%S')
        self.arrival = datetime. strptime(
            data['arrival'], '%Y-%m-%dT%H:%M:%S')

    def __repr__(self):
        return f'({self.id}: {self.start} > {self.end})'


def convert_to_hours(seconds):
    minutes = seconds / 60
    hours = minutes / 60
    return hours


def get_edges(csv_read):
    list = [Flight(id, x) for id, x in enumerate(csv_read)]
    edges = []
    for x in list:
        for y in list:
            if x.end == y.start:
                # Layover between arrival and departure 6h max 1h min
                layover_time = x.arrival - y.departure
                hours = convert_to_hours(layover_time.total_seconds())
                if hours <= 6 and hours >= 1:
                    edges.append((x, y))

    return edges


def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start not in graph:
        return []
    elif start == end:
        return [path]
    else:
        paths = []
        for node in graph[start]:
            if node not in path:
                newpaths = find_all_paths(graph, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
    return paths


def get_nodes(edges):
    nodes = []
    for edge in edges:
        for i in range(0, 1):
            if edge[i] not in nodes:
                nodes.append(edge[i])
    return nodes


if __name__ == '__main__':
    csv_file = open('./examples/example2.csv')
    csv_read = csv.DictReader(csv_file, delimiter=',')

    # I. Create Nodes and Edges
    edges = get_edges(csv_read)
    nodes = get_nodes(edges)

    # Create Graph
    graph = {}
    for node in nodes:
        graph[node] = []

    for edge in edges:
        graph[edge[0]].append(edge[1])

    for i in graph:
        print('flight:')
        print(i)
        # print('connecting flights')
        # print(graph[i])
        # print('----------')

    print()
    print()
    start = 'GXV'
    end = 'LOM'

    print(start, end)

    starting_points = [x for x in nodes if x.start == start]
    ending_points = [x for x in nodes if x.end == end]

    print('starting_points: ', len(starting_points))
    print('ending_points: ', len(ending_points))
    print('combination ', len(starting_points) * len(ending_points))
    routes = []
    for start_ in starting_points:
        for end_ in ending_points:
            for path in find_all_paths(graph, start_, end_):
                routes.append(path)

    print('number of routes to destination: ', len(routes))

    # step 3
    # No repeating airports in the same trip!
    # A -> B -> A -> C is not a valid combination for search A -> C.

    unique_trips = []
    for route in routes:
        trip = [start]+[x.end for x in route]
        if len(set(trip)) == len(trip):
            unique_trips.append(route)

    print('number of unique routes: ', len(unique_trips))

    print()

    results = []

    for route in unique_trips:
        print(route)
        row = {
            "flights": [],
            "bags_allowed": 1,
            "bags_count": 1,
            "destination": "REJ",
            "origin": "BTW",
            "total_price": 110.0,
            "travel_time": "6:55:00"
        },
        results.append(row)
