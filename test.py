import os, json

test_cases = json.load(open("./test_cases_3.json"))
for i in test_cases:
    print("test_case: ", i["test_case"])
    print("--------------------------------------------------")
    bags = i.get("bags", None)
    return_flight = i.get("return_flight", None)
    layovers = i.get("layovers", None)
    departure_time = i.get("departure_time", None)
    display = i.get("display", None)

    optional = " "
    optional += f" --bags={bags}" if bags is not None else ""
    optional += f" --return_flight={return_flight}" if return_flight is not None else ""
    optional += f" --layovers={layovers}" if layovers is not None else ""
    optional += (
        f" --departure_time={departure_time}" if departure_time is not None else ""
    )
    command = f"python -m solution {i['file_path']} {i['origin']} {i['destination']} {optional}"
    print(command)
    os.system(command)
