import argparse
import sys
import os
from datetime import datetime
import csv


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

    parser.add_argument("--bags", help="Number of bags allowed", type=int)
    parser.add_argument("--layovers", help="Number of layovers allowed", type=int)
    parser.add_argument("--departure_time", help="Number of bags allowed", type=str)
    parser.add_argument("--return_flight", help="display return flights", type=str)
    args = parser.parse_args()

    return args


def validate_inputs(args):
    # Check if file exists
    if not os.path.exists(args.file_path):
        print("file could not be found")
        sys.exit()

    if os.path.exists(args.file_path):
        csv_read = csv.DictReader(open(args.file_path), delimiter=",")
        for i in csv_read:
            if len(i) != 8:
                print("file is missing columns")
                sys.exit()

    # Check if Origin and Destination are correctly formatted
    if len(args.origin) != 3 or len(args.destination) != 3:
        print("Airport code can not be longer or shorter than 3 characters")
        sys.exit()

    # Check if Origin and Destination are string
    if not isinstance(args.origin, str) or not isinstance(args.destination, str):
        print("Airports should be of type String")
        sys.exit()

    # Number of bags, check if values are int
    if "bags" in args:
        if args.bags:
            try:
                args.bags = int(args.bags)
            except:
                print("Bags should be of type Integer")
                sys.exit()

    if "return_flight" in args:
        if args.return_flight:
            if args.return_flight == "True":
                args.return_flight = True
            elif args.return_flight == "False":
                args.return_flight = False
            else:
                print("Return should be of type bool (True / False)")
                sys.exit()

    if "departure_time" in args:
        if args.departure_time:
            try:
                args.departure_time = datetime.strptime(
                    args.departure_time, "%Y-%m-%dT%H:%M:%S"
                )
            except Exception:
                print("Can not convert departure time")
                sys.exit()

    if "layovers" in args:
        if args.layovers is not None:
            try:
                args.layovers = int(args.layovers)
            except:
                print("Layovers should be of type Integer")
                sys.exit()
