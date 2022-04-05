import csv
from datetime import datetime


class FlightGraph:


class Flight:
    def __init__(self, data):
        self.start = data['origin']
        self.end = data['destination']

    def __repr__(self):
        return f'{self.start} > {self.end}'


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
