from package.main import *

if __name__ == "__main__":
    timer = time.time()
    args = start_parser()
    validate_inputs(args)
    graph = Graph(args.file_path)
    routes = get_routes(graph, args.origin, args.destination)
    sorted_results = render_results(routes, args.origin, args.destination, args.bags)

    print(json.dumps(sorted_results, indent=2))
    print(len(sorted_results))
    print(f"search_duration: { round(time.time() - timer, 2) }")
    print("")
    print("")
    print("")
