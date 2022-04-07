import time
from package.ascii_art import *
from package.validation import start_parser, validate_inputs
from package.graph import Graph
from package.rendering import render_results

if __name__ == "__main__":

    timer = time.time()

    # I. Get Arguments
    args = start_parser()

    ## II. Validate Inputs
    validate_inputs(args)

    # II. Get Graph (which calculates the routes)
    graph = Graph(
        args.file_path,
        args.origin,
        args.destination,
        args.bags,
        args.layovers,
        args.departure_time,
    )

    # IV. Take the routes and render them
    for route in graph.routes:
        print(route)

    sorted_results = render_results(
        graph.routes, args.origin, args.destination, args.return_flight
    )
    # print(json.dumps(sorted_results, indent=2))
    # print(len(sorted_results))
    print(f"search_duration: { round(time.time() - timer, 2) }")
