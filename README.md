# Suspension Report
Days from Suspension Report. Generates reports in ``csv`` format based an spreadsheet 

### Tech

The application is built on ``Python 3.8`` with no external or 3rd party models required

### Run

```sh
$ python app.py "path/to/csvfile" "path/to/empty/folder"
```
File name format example
```sh
2019_04_08_payments.csv
```
### Tests

```sh
$ python -m unittest discover
```

### Thought Process
> Keep things as simple as possible
> Application Structure simple and easy to follow
> Separate the bootstrap so that the application can be started from a different *mode* like an API
> Handle Exceptions Exceptionally
> Validate before transacting
> Keep things consistent
> Make things reusable

#### Suspension Algorithm
> Base mostly around simple date calculations. First thing was to estiblish the date of the last payment and to look foward 90+ days. Second was to get the the list sorted with a simple lambda function
#### The Agent Collection Algorithm
> The Agent Collection report plays with dictionaries uses a key which consist of relevent fields so keep track of the totals. After which it would be split into its constituant parts to prepare it to be written to csv
### The Payment Type Report
> This follows the same structure as the Agent Collection report where using dictionary keys to keep track of items

License
----

MIT


