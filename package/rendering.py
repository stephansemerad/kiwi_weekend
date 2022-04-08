def render_results(
    unique_routes,
    start,
    end,
    bags=0,
    layovers=0,
    return_flight=False,
):
    results = []
    for route in unique_routes:
        travel_time = None
        travel_start = None
        travel_end = None
        bags_allowed = None
        flights = []
        total_price = 0

        for flight in route:
            print(flight)
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
            "flights": flights,
            "bags_allowed": bags_allowed,
            "bags_count": bags,
            "origin": start,
            "destination": end,
            "total_price": total_price,
            "travel_time": str(travel_time),
        }
        results.append(row)

    sorted_results = sorted(results, key=lambda d: float(d["total_price"]))
    return sorted_results
