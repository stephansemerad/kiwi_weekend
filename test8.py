import json
import csv
import os
from solution.main import Flight


class Graph:
    def __init__(self, csv_data):
        self.edges = self.get_edges(csv_data)
        self.nodes = self.get_nodes(self.edges)
        self.graph = self.get_graph(self.nodes, self.edges)

    def get_edges(self, csv_read):
        list = [Flight(id, x) for id, x in enumerate(csv_read)]
        edges = []
        for x in list:
            for y in list:
                if x.end == y.start:
                    # Layover between arrival and departure 6h max 1h min
                    layover_time = y.departure - x.arrival
                    hours = (layover_time.total_seconds() / 60) / 60
                    if hours <= 6 and hours >= 1:
                        edges.append((x, y))

        return edges

    def get_nodes(self, edges):
        nodes = []
        for edge in edges:
            for i in range(0, 1):
                if edge[i] not in nodes:
                    nodes.append(edge[i])
        return nodes

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


if __name__ == '__main__':

    print()
    print('parameters')

    csv_file = open('./examples/example2.csv')
    start = 'GXV'
    end = 'LOM'
    bags_count = 0
    retour = 0

    csv_read = csv.DictReader(csv_file, delimiter=',')

    # II. Create Graph
    graph = Graph(csv_read)
    print(graph.graph)

    # # II. Starting and Ending Points
    # starting_points = [x for x in nodes if x.start == start]
    # ending_points = [x for x in nodes if x.end == end]

    # print('starting_points: ', len(starting_points))
    # print('ending_points: ', len(ending_points))
    # print('combination ', len(starting_points) * len(ending_points))

    # # Iv. Loop over starting points  and ending_point + recursive call over graph
    # routes = []
    # for start_ in starting_points:
    #     for end_ in ending_points:
    #         for path in find_all_paths(graph, start_, end_):
    #             routes.append(path)

    # print('number_of_possible_routes_to_destination: ', len(routes))

    # # VI. Cleaning of routes to not have repeating flights
    # # No repeating airports in the same trip!

    # unique_trips = []
    # for route in routes:
    #     trip = [start]+[x.end for x in route]
    #     if len(set(trip)) == len(trip):
    #         unique_trips.append(route)

    # print('number_of_unique_routes: ', len(unique_trips))

    # # VII. Rendering of results
    # results = []
    # for route in unique_trips:
    #     total_price = 0
    #     travel_time = None
    #     travel_start = None
    #     travel_end = None
    #     bags_allowed = None

    #     flights = []

    #     total_price = 0

    #     for flight in route:
    #         flights.append(flight.export_to_json())
    #         total_price += flight.base_price

    #         if travel_start is None:
    #             travel_start = flight.departure
    #         travel_end = flight.arrival

    #     travel_time = travel_end - travel_start

    #     row = {
    #         'route': str(route),
    #         "flights": flights,
    #         "bags_allowed": str(bags_allowed),
    #         "bags_count": str(bags_count),
    #         "origin": str(start),
    #         "destination": str(end),
    #         "total_price": total_price,
    #         "travel_start": str(travel_start),
    #         "travel_end": str(travel_end),
    #         "travel_time": str(travel_time)
    #     }
    #     results.append(row)

    # # VIII. Sorting of the results by price
    # sorted_results = sorted(results, key=lambda d: float(d['total_price']))

    # # IV . Display
    # print(json.dumps(sorted_results, indent=2))
