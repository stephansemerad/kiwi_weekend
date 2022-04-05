import json
import csv
import os

from solution.solution import *


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
                layover_time = y.departure - x.arrival
                hours = convert_to_hours(layover_time.total_seconds())
                if hours <= 6 and hours >= 1:
                    print(layover_time)
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
                new_paths = find_all_paths(graph, node, end, path)
                for new_path in new_paths:
                    paths.append(new_path)
    return paths


def get_nodes(edges):
    nodes = []
    for edge in edges:
        for i in range(0, 1):
            if edge[i] not in nodes:
                nodes.append(edge[i])
    return nodes


if __name__ == '__main__':

    print()
    print('parameters')

    csv_file = open('./examples/example2.csv')
    start = 'GXV'
    end = 'LOM'
    bags_count = 0
    retour = 0

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

    # for i in graph:
    #     print('flight:')
    #     print(i)
    #     print('connecting flights')
    #     print(graph[i])
    #     print('----------')

    print()

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
        total_price = 0
        travel_time = None
        bags_allowed = None

        flights = []
        travel_start = travel_end = None
        total_price = 0
        for flight in route:
            flights.append(flight.export_to_json())
            total_price += flight.base_price

            if travel_start is None:
                travel_start = flight.departure
            travel_end = flight.arrival

        travel_time = travel_end - travel_start

        row = {
            'route': str(route),
            # "flights": flights,
            # "bags_allowed": str(bags_allowed),
            # "bags_count": str(bags_count),
            # "origin": str(start),
            # "destination": str(end),
            "total_price": total_price,
            "travel_start": str(travel_start),
            "travel_end": str(travel_end),

            "travel_time": str(travel_time)
        }
        results.append(row)


for result in results:
    print(results)

sorted_results = sorted(results, key=lambda d: float(d['total_price']))
print(json.dumps(sorted_results, indent=2))


# my_list = [{'name': 'Homer', 'age': 39}, {'name': 'Bart', 'age': 10}, {
#     'name': 'Maggie', 'age': 1}, {'name': 'Lisa', 'age': 12}, {'name': 'Marge', 'age': 30}, ]
#
