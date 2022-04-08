import time, json
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
    oneway_graph = Graph(
        args.file_path,
        args.origin,
        args.destination,
        args.bags,
        args.layovers,
        args.departure_time,
    )

    # II.I Check if return flights should be applied
    print()
    routes = []
    if args.return_flight == True:
        return_routes = Graph(
            args.file_path,
            args.destination,
            args.origin,
            args.bags,
            args.layovers,
            args.departure_time,
        )
        for oneway_flight in oneway_graph.routes:
            for return_flight in return_routes.routes:
                oneway_arrival = oneway_flight[-1].arrival
                return_departure = return_flight[0].departure
                layover_return = return_departure - oneway_arrival
                hours = layover_return.total_seconds() / 60 / 60
                if hours >= 1:
                    routes.append(oneway_flight + return_flight)
    else:
        routes = oneway_graph.routes

    # # IV. Take the routes and render them
    sorted_results = render_results(
        routes, args.origin, args.destination, args.return_flight
    )
    print(json.dumps(sorted_results, indent=2))
    print(len(sorted_results))
    print()
    print(f"search_duration: { round(time.time() - timer, 2) }")
