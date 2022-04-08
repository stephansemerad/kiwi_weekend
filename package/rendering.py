def render_results(
    unique_routes,
    start,
    end,
    bags,
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

        for step in route:
            flights.append(step.export_to_json())

            # calculate the total price for bags per flight
            bag_price = 0
            if bags:
                bag_price = step.bag_price * bags

            total_price += step.base_price + bag_price

            # get travel start
            if travel_start is None:
                travel_start = step.departure
            travel_end = step.arrival

            # looping through bags to identify the one with the lowest.
            if bags_allowed is None:
                bags_allowed = step.bags_allowed
            else:
                if step.bags_allowed < bags_allowed:
                    bags_allowed = step.bags_allowed

        # getting the travel time for each flight.
        travel_time = travel_end - travel_start
        row = {
            "flights": flights,
            "bags_allowed": bags_allowed,
            "bags_count": 0 if bags == None else bags,
            "origin": start,
            "destination": end,
            "total_price": total_price,
            "travel_time": str(travel_time),
            "return_flight": return_flight,
        }
        results.append(row)

    sorted_results = sorted(results, key=lambda d: float(d["total_price"]))
    return sorted_results
