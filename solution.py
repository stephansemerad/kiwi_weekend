import sys
import csv
import json
import argparse
from unittest import result

class Flight():
    def __init__(self, data):
        self.flight_no = data['flight_no']
        self.origin = data['origin']
        self.destination = data['destination']
        self.departure = data['departure']
        self.arrival = data['arrival']
        self.base_price = data['base_price']
        self.bag_price = data['bag_price']
        self.bags_allowed = data['bags_allowed']
    
    def __repr__(self):
        return f' ( {self.origin} > {self.destination})'
    
class KiwiSearch:
    def __init__(self, from_airport, to_airport, bags=0):
        self.from_airport = from_airport
        self.to_airport = to_airport
        self.bags = bags
        self.file_path = './examples/example0.csv'
        self.results = []
        
    def search(self):
        print('search')
        csv_file = open(self.file_path)
        csv_read = csv.DictReader(csv_file, delimiter=',')
        data = [Flight(x) for x in csv_read]
        
        print(type(data))


        print(len(data))
        # 1 Search Direct Flights and remove them. 
        direct_flights = []
        for index, flight in enumerate(data):
            if flight.origin == self.from_airport and flight.destination == self.to_airport:
                direct_flights.append(flight)
                data.pop(index)
                
        # 2. Get the starting point of possible indirect flights and remove them from the data.
        print(len(data))
        starting_points = []
        for index, flight in enumerate(data):
            if flight.origin == self.from_airport:
                starting_points.append(flight)
                data.pop(index)
    
        # 3. Loop through the starting points and recursively search for 
        # indirect flights until reaching to the base (to_airport).
        def get_connections(flight, data):
            connections = []
            for possible_connection in data:
                if possible_connection.origin == flight.destination:
                    connections.append(possible_connection)
            return connections
            
        for flight in starting_points:
            print('flight : ', flight)
            connections = get_connections(flight, data)
            print('possible_connection : ', connections)
            
        
        # for index, flight in enumerate(data):
        #     find_connection(flight, flight.destination, data)
                
        # print(json.dumps(direct_flights, indent=4, sort_keys=True))

        # print(starting_list)
            
        # step 2: get all possible combinations until reaching the destination airport
        
        # step 3: make sure these make sense according to the rules. 
        
        # step 4: render the result.


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--from', dest='from_airport' )
    parser.add_argument('--to', dest='to_airport')
    parser.add_argument('--bags', dest='bags')
    parser.add_argument('--return', dest='return')

    args = parser.parse_args()
    print (f'from_airport: {args.from_airport} | to_airport: {args.to_airport} | bags: {args.bags}')

    search = KiwiSearch(args.from_airport, args.to_airport, args.bags)
    search.search()