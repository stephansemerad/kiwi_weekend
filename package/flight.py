import json
import csv
import os
import re
import time
from datetime import datetime


class Flight:
    def __init__(self, id, data):
        self.id = id
        self.flight_no = data["flight_no"]
        self.start = data["origin"]
        self.end = data["destination"]

        self.origin = data["origin"]
        self.destination = data["destination"]

        self.departure = self.str_datetime(data["departure"])
        self.arrival = self.str_datetime(data["arrival"])
        self.base_price = float(data["base_price"])
        self.bag_price = float(data["bag_price"])
        self.bags_allowed = int(data["bags_allowed"])

    def __repr__(self):
        return f"({self.id}: {self.flight_no} FROM {self.start} {self.departure} > TO {self.end} {self.arrival}  [{self.arrival- self.departure}] [bags: {self.bags_allowed}]  )"

    def str_datetime(self, date_string):
        return datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S")

    def export_to_json(self):
        return (
            {
                "flight_no": self.flight_no,
                "origin": self.origin,
                "destination": self.destination,
                "departure": self.departure.strftime("%Y-%m-%dT%H:%M:%S"),
                "arrival": self.arrival.strftime("%Y-%m-%dT%H:%M:%S"),
                "base_price": self.base_price,
                "bag_price": self.bag_price,
                "bags_allowed": self.bags_allowed,
            },
        )
