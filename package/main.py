import json
import csv
import os
import re
import sys
import time
import argparse
from datetime import datetime


class Flight:
    def __init__(self, id, data):
        self.id = id
        self.flight_no = data["flight_no"]
        self.start = data["origin"]
        self.end = data["destination"]

        self.origin = data["origin"]
        self.destination = data["destination"]

        self.departure = self.str_datetime(data["departure"])
        self.arrival = self.str_datetime(data["arrival"])
        self.base_price = float(data["base_price"])
        self.bag_price = float(data["bag_price"])
        self.bags_allowed = int(data["bags_allowed"])

    def __repr__(self):
        # return f"({self.id}: {self.flight_no} {self.start} {self.departure} > {self.end} {self.arrival} [{self.arrival- self.departure}])"

        return f"({self.id}: {self.start} > {self.end})"

    def str_datetime(self, date_string):
        return datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S")

    def export_to_json(self):
        return (
            {
                "flight_no": str(self.flight_no),
                "origin": str(self.origin),
                "destination": str(self.destination),
                "departure": str(self.departure),
                "arrival": str(self.arrival),
                "base_price": self.base_price,
                "bag_price": self.bag_price,
                "bags_allowed": self.bags_allowed,
            },
        )


class Graph:
    def __init__(self, csv_path):
        self.csv_read = csv.DictReader(open(csv_path), delimiter=",")
        self.nodes, self.edges = self.get_nodes_and_edges(self.csv_read)
        self.graph = self.get_graph(self.nodes, self.edges)

    def get_nodes_and_edges(self, csv_read):
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
    unique = list(set([x.start for x in path]))
    if len(path) != len(unique):
        return []
    elif end.destination in unique:
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


def get_routes(graph, from_, to_):
    starting_points = [x for x in graph.nodes if x.start == from_]
    ending_points = [x for x in graph.nodes if x.end == to_]
    routes = []
    for from_ in starting_points:
        for to_ in ending_points:
            for path in find_all_paths(graph.graph, from_, to_):
                routes.append(path)
    return routes


def render_results(unique_routes, start, end, bags=0):
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

            bag_price = 0
            if bags:
                bag_price = flight.bag_price * bags

            total_price += flight.base_price + bag_price

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
            "route": str(route),
            "flights": flights,
            "bags_allowed": str(bags_allowed),
            "bags_count": str(bags),
            "origin": str(start),
            "destination": str(end),
            "total_price": total_price,
            "travel_start": str(travel_start),
            "travel_end": str(travel_end),
            "travel_time": str(travel_time),
        }
        results.append(row)

    sorted_results = sorted(results, key=lambda d: float(d["total_price"]))
    return sorted_results


def start_parser():
    parser = argparse.ArgumentParser(description="Flight search")
    parser.add_argument(
        "file_path", metavar="file_path", type=str, help="File path for the csv "
    )
    parser.add_argument(
        "origin", metavar="origin", type=str, help="Origin Airport Code (3 Char)"
    )
    parser.add_argument(
        "destination",
        metavar="destination",
        type=str,
        help="Destination Airport Code (3 Char)",
    )

    parser.add_argument("--bags", help="Number of bags allowed", default=0, type=int)
    parser.add_argument("--layovers", help="Number of layovers allowed", type=int)
    parser.add_argument("--departure_time", help="Number of bags allowed", type=str)
    parser.add_argument(
        "--return_flight", help="Should retun flight should be displayed ", type=bool
    )
    args = parser.parse_args()
    return args


def validate_inputs(args):
    # Check if file exists
    if not os.path.exists(args.file_path):
        print("file could not be found")
        sys.exit()

    # Check if Origin and Destination are correctly formatted
    if len(args.origin) > 3 or len(args.destination) > 3:
        print("Airport code can not be longer than 3 characters")
        sys.exit()

    # Check if Origin and Destination are string
    if not isinstance(args.origin, str) or not isinstance(args.destination, str):
        print("Airports should be of type String")
        sys.exit()

    if "bags" in args:
        if isinstance(args, int):
            print("Bags should be of type Integer")
            sys.exit()

    if "return_flight" in args:
        if isinstance(args, bool):
            print("Return should be of type bool")
            sys.exit()

    if "departure_dt" in args:
        if args.departure_dt:
            pass
        # print("checking departure")
        # sys.exit()

    if "layovers" in args:
        if isinstance(args, int):
            print("Layovers should be of type Integer")
            sys.exit()
