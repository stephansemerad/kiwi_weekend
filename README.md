# kiwi_weekend

## Search Flight Options based on csv files.

Looking for PyCon CZ, I came over a interesting python gettogether from Kiwi.com <br>
(https://code.kiwi.com/pythonweekend/), to be able to attend I have submitted below code.

## How to use

Essentially from the directory you call it in the manner below,

```bash
python -m solution [file_path] [origin_airport] [destination_airport]

python -m solution ./examples/example3.csv EZO JBN
```

| Optional Argument                      | Description                                                         |
| -------------------------------------- | ------------------------------------------------------------------- |
| `--bags=2`                             | Check flights for the allowed bags and only shows the ones matching |
| `--return_flight=True`                 | Return flights being renderes (Based on Arrival time + 1 day)       |
| `--layovers=1`                         | Limits the routes suggested to the number of layovers               |
| `--departure_time=2021-09-04T04:20:00` | Sets a given Departure time and filters the results by it           |

# How it all works

#### Step 1 - Args and Validation

#### Step 2 - Building a Graph with objects, and runnigning the recurssion.

#### Step 3 - Returning the result

# Images

![](https://raw.githubusercontent.com/stephansemerad/National-Bank-of-Poland-Rates/master/pln_fx/api.png)

![](https://raw.githubusercontent.com/stephansemerad/National-Bank-of-Poland-Rates/master/pln_fx/api.png)

# Links

[https://github.com/kiwicom/python-weekend-entry-task](https://github.com/kiwicom/python-weekend-entry-task)<br />
[https://github.com/stephansemerad/kiwi_weekend](https://github.com/stephansemerad/kiwi_weekend)
