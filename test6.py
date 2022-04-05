import csv
from datetime import datetime


class Flight():
    def __init__(self, data):
        self.start = data['origin']
        self.end = data['destination']

    def __repr__(self):
        return f'{self.start} > {self.end}'

    def connection_flights(self, data, start, end, path=[]):
        print('connection_flights')
        connection_flights = []
        print(data)
        return connection_flights

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


csv_file = open('./examples/example0.csv')
csv_read = csv.DictReader(csv_file, delimiter=',')
data = [Flight(x) for x in csv_read]


def get_possible_routs(graph, start, end):
    routes = []
    for path in find_all_paths(graph, start, end):
        routes.append(path)
    return routes


start = 'WIW'
end = 'ECV'

routes = get_possible_routs(data, start, end)
