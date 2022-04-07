import os, json

test_cases = json.load(open("test_cases_2.json"))
for i in test_cases:
    print()
    print("test_case: ", i["test_case"])
    print("--------------------------------------------------")
    bags = i.get("bags", None)
    return_flight = i.get("return_flight", None)
    layovers = i.get("layovers", None)
    departure_dt = i.get("departure_dt", None)

    optional = " "
    if bags:
        optional += f" --bags={bags}"
    if return_flight:
        optional += f" --return_flight={return_flight}"
    if layovers:
        optional += f" --layovers={layovers}"
    if departure_dt:
        optional += f" --departure_time={departure_dt}"

    command = f"python -m solution {i['file_path']} {i['origin']} {i['destination']} {optional}"
    print(command)
    os.system(command)
