from package.validation import *
from package.flight import *
from package.graph import *
from package.rendering import *


class Graph:
    def __init__(
        self,
        csv_path,
        origin,
        destination,
        bags=None,
        layovers=None,
        departure_time=None,
    ):
        self.csv_path = csv_path
        self.origin = origin
        self.destination = destination
        self.bags = bags
        self.layovers = layovers
        self.departure_time = departure_time

        self.csv_read = csv.DictReader(open(csv_path), delimiter=",")
        self.nodes, self.edges = self.get_nodes_and_edges()
        self.graph = self.get_graph()
        self.routes = self.get_routes()

    def __repr__(self):
        return f"[{self.origin} > {self.destination}] [bags: {self.bags}] [layovers: {self.layovers}] [departure_time: {self.departure_time}]"

    def get_nodes_and_edges(self):
        list = [Flight(id, x) for id, x in enumerate(self.csv_read)]

        # if bag arg was given, create a new list with only flights that allow the amount of bags.
        if self.bags:
            list = [i for i in list if i.bags_allowed >= self.bags]

        # if departure_time was give, create a new list with only flights that depart after the given time.
        if self.departure_time:
            list = [i for i in list if i.departure >= self.departure_time]

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

    def get_graph(self):
        graph = {}
        for node in self.nodes:
            graph[node] = []
        for edge in self.edges:
            graph[edge[0]].append(edge[1])
        return graph

    def find_all_paths(self, start, end, path=[]):
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
            for node in self.graph[start]:
                if node not in path:
                    new_paths = self.find_all_paths(node, end, path)
                    for new_path in new_paths:
                        paths.append(new_path)

            return paths

    def get_routes(self):
        starting_points = [x for x in self.nodes if x.start == self.origin]
        ending_points = [x for x in self.nodes if x.end == self.destination]
        routes = []
        for start in starting_points:
            for end in ending_points:
                for path in self.find_all_paths(start, end):
                    routes.append(path)
        return routes


if __name__ == "__main__":

    kiwi = """
    __   .__        .__ 
    |  | _|__|_  _  _|__|
    |  |/ /  \ \/ \/ /  |
    |    <|  |\     /|  |
    |__|_ \__| \/\_/ |__|
        \/       
    """
    print(kiwi)

    timer = time.time()
    # I. Get Arguments and check them
    args = start_parser()
    validate_inputs(args)

    # II. Get Graph
    graph = Graph(
        args.file_path,
        args.origin,
        args.destination,
        args.bags,
        args.layovers,
        args.departure_time,
    )
    print(graph)
    print(graph.routes)
    print(len(graph.routes))

    # routes = get_routes(graph, args.origin, args.destination)

    # print(args.display)
    # sorted_results = render_results(routes, args.origin, args.destination, args.bags)
    # print(json.dumps(sorted_results, indent=2))
    # print(len(sorted_results))
    print(f"search_duration: { round(time.time() - timer, 2) }")
