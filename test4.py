import csv
from datetime import datetime


class Flight():
    def __init__(self, data):
        self.parent = data['origin']
        self.child = data['destination']

    def __repr__(self):
        return f'{self.start} > {self.end}'

    def connection_flights(self, to, graph):
        print('connection_flights')
        connection_flights = []
        print(graph)
        return connection_flights


def create_graph():
    csv_file = open('./examples/example0.csv')
    csv_read = csv.DictReader(csv_file, delimiter=',')
    data = [Flight(x) for x in csv_read]

    graph = {}  # Graph is a dictionary to hold our child-parent relationships.
    for flight in data:
        graph[flight.parent] = []

    for flight in data:
        if flight.child not in graph[flight.parent]:
            graph[flight.parent].append(flight.child)

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
                newpaths = find_all_paths(graph, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
    return paths


def get_possible_routs(graph, start, end):
    routes = []
    for path in find_all_paths(graph, start, end):
        # print('|'.join(path))
        routes.append(path)
    return routes


def reformat_routes(routes):
    result = []
    for route in routes:
        new_route = []
        for i in range(0, len(route)-1):
            new_route.append([route[i], route[i+1]])
        result.append(new_route)
    return result


if __name__ == '__main__':
    start = 'WIW'
    end = 'RFZ'
    graph = create_graph()
    routes = get_possible_routs(graph, start, end)
    routes = reformat_routes(routes)
    for route in routes:
        print(route)
        print('----------------------')
        for step in route:
            print(step)
