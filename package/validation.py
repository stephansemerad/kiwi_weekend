import argparse
import sys
import os
from datetime import datetime


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
    parser.add_argument("--return_flight", help="display return flights", type=bool)
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

    # Number of bags, check if values are int
    if "bags" in args:
        try:
            args.bags = int(args.bags)
        except:
            print("Bags should be of type Integer")
            sys.exit()

    if "return_flight" in args:
        try:
            args.return_flight = bool(args.return_flight)
        except:
            print("Return should be of type bool")
            sys.exit()

    if "departure_time" in args:
        try:
            args.departure_time = datetime.strptime(
                args.departure_time, "%Y-%m-%dT%H:%M:%S"
            )
        except Exception:
            print("Can not convert departure time")
            sys.exit()

    if "layovers" in args:
        try:
            args.layovers = int(args.layovers)
        except:
            print("Layovers should be of type Integer")
            sys.exit()
