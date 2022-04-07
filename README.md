# kiwi_weekend

#### search results based on csv files.

Looking for PyCon CZ, I came over a interesting python get together from Kiwi.com (https://code.kiwi.com/pythonweekend/), to be able to attend I have hereby submitted below code.

#### How to user

Essentially from the directory you call it in the manner below,

```bash
python -m solution [file_path] [origin_airport] [destination_airport]

python -m solution ./examples/example3.csv EZO JBN
```

#### Optional Arguments

| Optional Argument                      | Description                                                         |
| -------------------------------------- | ------------------------------------------------------------------- |
| `--bags=2`                             | Check flights for the allowed bags and only shows the ones matching |
| `--return_flight=True`                 | Return flights being renderes (Based on Arrival time + 1 day)       |
| `--layovers=1`                         | Limits the routes suggested to the number of layovers               |
| `--departure_time=2021-09-04T04:20:00` | Sets a given Departure time and filters the results by it           |

![](https://raw.githubusercontent.com/stephansemerad/National-Bank-of-Poland-Rates/master/pln_fx/api.png)

# How it all works

# Links

[https://github.com/kiwicom/python-weekend-entry-task](https://github.com/kiwicom/python-weekend-entry-task)<br />
[https://github.com/stephansemerad/kiwi_weekend](https://github.com/stephansemerad/kiwi_weekend)
