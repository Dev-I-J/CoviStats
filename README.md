# CoviStats

CoviStats is a free CLI tool to get the latest COVID-19 statistics.

```text
D:\Dev\CoviStats> covistats --help
Usage: covistats [OPTIONS] COMMAND [ARGS]...

  A Simple CLI Tool To Get The Latest COVID-19 Statistics.

Options:
  -V, --version  Show the version and exit.
  -h, --help     Show this message and exit.

Commands:
  active          Get total active cases.
  all-data        Show statistics of all countries.
  confirmed       Get total confirmed cases.
  country-id      Get statistics of given country id (run 'covistats...
  country-name    Get statistics of given country (run 'covistats...
  country-rank    Get statistics of the country of the given rank.
  deaths          Get total deaths.
  list-countries  List all available countries.
  recovered       Get number of total recovered patients.
  total           Get number of total confirmed cases, active cases, deaths...
```

## Features

As of the current latest stable version - 0.0.1, covistats has the following outstanding features:

* Uses accurate data from [The John Hopkins University Coronavirus Resource Center](https://coronavirus.jhu.edu/)
* Useful `--help` option to get detailed help on the tool's commands.
* Outputs nicely colored and tabulated data for the user's convenience.
* Can get statistics by supplying either the country name, id or rank.
* Last updated time is displayed in result set if `-v` or `--verbose` is supplied.
* Relatively small computer resource usage.
* Fast execution.

## Installation

* Download the latest release for your os form [Github Releases](https://github.com/Dev-I-J/CoviStats/releases/latest).
* Extract the archive to any folder you like (It's recommended to add this folder to the `PATH` environment variable).

## Build From Source

* Clone repo: `git clone https://github.com/Dev-I-J/CoviStats.git`
* `cd` to project directory: `cd CoviStats`
* Install `pipenv`: `pip install pipenv`
* Install dependencies: `pipenv install --dev`
* Build executable: `pyinstaller covistats.spec`
* Run `covistats`: `dist/covistats --help`

## Usage

### Execution

You can execute covistats by executing the `covistats` executable (`.exe` or unix executable):

```bash
covistats --help
```

### Options

* `--help`, `-h` - Show the help message and exit:

```bash
covistats --help
covistats -h
```

* `--version`, `-V` - Show the version and exit.

```bash
covistats --version
covistats -V
```

### Commands

* `all-data` - Show statistics of all countries:
  * `--help`, `-h` - Show help message and exit.
  * `--verbose`, `-v` - Enable verbose mode.

```bash
covistats all-data
covistats all-data -v
```

* `list-countries` - List all available countries:
  * `--help`, `-h` - Show help message and exit.
  * `--verbose`, `-v` - Enable verbose mode.

```bash
covistats list-countries
covistats list-countries -v
```

* `country-id` - Get statistics of given country id:
  * `--help`, `-h` - Show help message and exit.
  * `--verbose`, `-v` - Enable verbose mode.

```bash
covistats country-id
covistats country-id -v
```

* `country-name` - Get statistics of given country:
  * `--help`, `-h` - Show help message and exit.
  * `--verbose`, `-v` - Enable verbose mode.

```bash
covistats country-name
covistats country-name -v
```

* `country-rank` - Get statistics of the country of the given rank:
  * `--help`, `-h` - Show help message and exit.
  * `--verbose`, `-v` - Enable verbose mode.

```bash
covistats country-rank
covistats country-rank -v
```

* `active` - Get total active cases.
* `confirmed` - Get total confirmed cases.
* `deaths` - Get total deaths.
* `recovered` - Get number of total recovered patients.
* `total` - Get number of total confirmed cases, active cases, deaths and recovered patients.

## License

`CoviStats` is licensed under [GNU General Public License v3](https://github.com/Dev-I-J/CoviStats/blob/master/LICENSE.md).

## Developer Info

`CoviStats` is written in [`Python`](https://python.org).

### Dependencies

* [`click`](https://pypi.org/project/click)
* [`click-spinner`](https://pypi.org/project/click-spinner)
* [`click-help-colors`](https://pypi.org/project/click-help-colors)
* [`covid`](https://pypi.org/project/covid)
* [`colorama`](https://pypi.org/project/colorama)
* [`tabulate`](https://pypi.org/project/tabulate)

### Dev Dependencies

* [`pyinstaller`](https://pypi.org/project/pyinstaller)
* [`flake8`](https://pypi.org/project/flake8)
* [`autopep8`](https://pypi.org/project/autopep8)
* [`rope`](https://pypi.org/project/rope)
