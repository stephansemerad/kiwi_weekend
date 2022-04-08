# kiwi_weekend

## Search Flight Options based on csv files.

## How to use

Essentially from the directory you call it in the manner below,

```bash
python -m solution [file_path] [origin_airport] [destination_airport]

python -m solution ./examples/example3.csv EZO JBN
```

In case you need a description of all the arguments you can run in the

```bash
python -m solution -h
```

| Optional Argument                      | Description                                                         |
| -------------------------------------- | ------------------------------------------------------------------- |
| `--bags=2`                             | Check flights for the allowed bags and only shows the ones matching |
| `--return_flight=True`                 | Return flights being renderes (Based on Arrival time + 1 day)       |
| `--layovers=1`                         | Limits the routes suggested to the number of layovers               |
| `--departure_time=2021-09-04T04:20:00` | Sets a given Departure time and filters the results by it           |

# How it all works

#### Step 1 - Args and Validation

The first step is to set up of the command line with the optional parameters, this is dome under package/validation.py under the function. start_parser()

after the inputs are accepted they get checked in the function validate_inputs(args)

Here I check if the

- if filepath is correct
- if each row in the file has 8 columns
- if the origin and destination are of len 3 / String
- if bags is int
- if departure_time can be converted to dt object.
- if layovers are int

#### Step 2 - Building a Graph with objects, and runnigning the recurssion.

The next step I have done is to take each flight and convert it into an object and essetially create a graph. While I am doing this, I am already applying filtes of the number of bags allowed per flight and the departure time.

I then run a recursive function over this graph, (get_routes/ find_all_paths) that give me all of the routes that are possible.Once I have the routes I also apply the limit of the layovers in case that is provided.

As an additional step in Step 2.2, if you provide the return argument as True, I create a second graph with data, and again get the routes with the recursive function, and then I join the direct routes with the returns making sure that a return flight does not happen before the arrival, and that the return flight is a minimum of 1 Hour after the direct light.

(I was not sure on how to display a flight with return)

#### Step 3 - Returning the result

Once I have a list of all possible routes I render and sort the result.
While creating the results I pass bags and calculate the total based on each flight and bag price.

Please note that if return flight is applie origin and destination will be the same, but in flights you will see that the trip goes throught the destination airport.

Flights are being sorted by total price from low to high.

# Images

![](https://github.com/stephansemerad/kiwi_weekend/raw/main/imgs/capture.png)

# Links

[https://github.com/kiwicom/python-weekend-entry-task](https://github.com/kiwicom/python-weekend-entry-task)<br />
[https://github.com/stephansemerad/kiwi_weekend](https://github.com/stephansemerad/kiwi_weekend)
