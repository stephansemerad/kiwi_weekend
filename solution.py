import json
import csv
import os
import sys
import time
import argparse

from package.main import Flight


class Graph:
    def __init__(self, csv_data):
        self.nodes, self.edges = self.get_edges(csv_data)
        self.graph = self.get_graph(self.nodes, self.edges)

    def get_edges(self, csv_read):
        list = [Flight(id, x) for id, x in enumerate(csv_read)]
        edges = []
        nodes = []

        for x in list:
            if x not in nodes:
                nodes.append(x)
            for y in list:
                if x.end == y.start:
                    # Layover between arrival and departure 6h max 1h min
                    layover_time = y.departure - x.arrival
                    hours = (layover_time.total_seconds() / 60) / 60
                    if hours <= 6 and hours >= 1:
                        edges.append((x, y))

        return nodes, edges

    def get_graph(self, nodes, edges):
        graph = {}
        for node in nodes:
            graph[node] = []

        for edge in edges:
            graph[edge[0]].append(edge[1])
        return graph


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


def get_routes(graph, start, end):
    starting_points = [x for x in graph.nodes if x.start == start]
    ending_points = [x for x in graph.nodes if x.end == end]

    # get routes
    routes = []
    for start_ in starting_points:
        for end_ in ending_points:
            for path in find_all_paths(graph.graph, start_, end_):
                routes.append(path)

    # clearing of routes to not have repeating flights
    unique_routes = []
    for route in routes:
        trip = [start]+[x.end for x in route]
        if len(set(trip)) == len(trip):
            unique_routes.append(route)

    return unique_routes


def render_results(unique_routes):
    results = []
    for route in unique_routes:
        travel_time = None
        travel_start = None
        travel_end = None
        bags_allowed = None

        flights = []

        total_price = 0

        for flight in route:
            flights.append(flight.export_to_json())
            total_price += flight.base_price

            # get travel start
            if travel_start is None:
                travel_start = flight.departure
            travel_end = flight.arrival

            # looping through bags to identify the one with the lowest.
            if bags_allowed is None:
                bags_allowed = flight.bags_allowed
            else:
                if flight.bags_allowed < bags_allowed:
                    bags_allowed = flight.bags_allowed

        # getting the travel time for each flight.
        travel_time = travel_end - travel_start
        row = {
            'route': str(route),
            "flights": flights,
            "bags_allowed": str(bags_allowed),
            "bags_count": str(bags_count),
            "origin": str(start),
            "destination": str(end),
            "total_price": total_price,
            "travel_start": str(travel_start),
            "travel_end": str(travel_end),
            "travel_time": str(travel_time)
        }
        results.append(row)

    sorted_results = sorted(results, key=lambda d: float(d['total_price']))
    return sorted_results


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Flight search')
    parser.add_argument('file_path', metavar='file_path', type=str, help='File path for the csv ')
    parser.add_argument('origin', metavar='origin', type=str, help='Origin Airport Code (3 Char)')
    parser.add_argument('destination', metavar='destination', type=str, help='Destination Airport Code (3 Char)')
    parser.add_argument('--bags', dest='bags', action='store_const',  const=sum, default=0, help='Number of bags [0]')
    parser.add_argument('--return', dest='return', action='store_const', const=sum, default=False, help='Return flight [True / False]')
    
    args = parser.parse_args()
    print(args.file_path)
    print(args.origin)
    print(args.destination)
    
    # Check if file exists
    if not os.path.exists(args.file_path):
        print('file could not be found')
        sys.exit()
    
    # Check if Origin and Destination are correctly formatted
    if len(args.origin) > 3 or len(args.destination) > 3:
        print('Airport code can not be longer than 3 characters')
        sys.exit()
        
    if not isinstance(args.origin, str) or isinstance(args.destination, str):
        print('Airports should be of type String')

    if 'bags' in args:
        print('hello')
    
    
    # if not os.path.isdir(input_path):
    #     print('The path specified does not exist')
    #     sys.exit()



    # csv_path = './examples/example1.csv'
    # start = 'DHE'
    # end = 'NIZ'
    # bags_count = 1
    # retour = 0

    # timer = time.time()

    # # I. Create Graph
    # csv_file = file = open(csv_path)
    # csv_read = csv.DictReader(csv_file, delimiter=',')
    # graph = Graph(csv_read)

    # # II. Loop over starting points  and ending_point + recursive call over graph
    # unique_routes = get_routes(graph, start, end)

    # # III. Rendering of results
    # results = render_results(unique_routes)

    # # IV . Display
    # print(json.dumps(results, indent=2))
    # print(f'number_of_results: {len(results)}')
    # print(f"duration_of_search: { round(time.time() - timer, 2) }")
