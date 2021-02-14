# `click` imports
import click_help_colors
import click_spinner
import click

# Third party imports
import colorama
import tabulate
import covid

# Standard library imports
import datetime
import re

# Make colors work on windows
colorama.init()

# Variables for app name, app description and app version
app_name = "CoviStats"
app_version = "0.0.1-alpha"
app_description = "A Simple CLI Tool To Get The Latest COVID-19 Statistics."


# Helper for `all-data`
def __getAllCountriesData(verbose: bool) -> str:
    covid_data = covid.Covid()
    i = 0
    data = []
    for item in covid_data.get_data():
        i += 1
        if not verbose:
            data.append(
                (
                    click.style(str(i), fg="blue"),
                    click.style(str(item["id"]), fg="cyan"),
                    click.style(str(item["country"]), fg="bright_blue"),
                    click.style(
                        re.sub(
                            r'\B(?=(\d{3})+(?!\d))', ',',
                            str(item["confirmed"]
                                ) if item["confirmed"] is not None else "N/A"
                        ), fg="yellow"
                    ),
                    click.style(
                        re.sub(
                            r'\B(?=(\d{3})+(?!\d))', ',',
                            str(item["active"]
                                ) if item["active"] is not None else "N/A"
                        ), fg="magenta"
                    ),
                    click.style(
                        re.sub(
                            r'\B(?=(\d{3})+(?!\d))', ',',
                            str(item["deaths"]
                                ) if item["deaths"] is not None else "N/A"
                        ), fg="red"
                    ),
                    click.style(
                        re.sub(
                            r'\B(?=(\d{3})+(?!\d))', ',',
                            str(item["recovered"]
                                ) if item["recovered"] is not None else "N/A"
                        ), fg="green"
                    )
                )
            )
        else:
            data.append(
                (
                    click.style(str(i), fg="blue"),
                    click.style(str(item["id"]), fg="cyan"),
                    click.style(str(item["country"]), fg="bright_blue"),
                    click.style(
                        re.sub(
                            r'\B(?=(\d{3})+(?!\d))', ',',
                            str(item["confirmed"]
                                ) if item["confirmed"] is not None else "N/A"
                        ), fg="yellow"
                    ),
                    click.style(
                        re.sub(
                            r'\B(?=(\d{3})+(?!\d))', ',',
                            str(item["active"]
                                ) if item["active"] is not None else "N/A"
                        ), fg="magenta"
                    ),
                    click.style(
                        re.sub(
                            r'\B(?=(\d{3})+(?!\d))', ',',
                            str(item["deaths"]
                                ) if item["deaths"] is not None else "N/A"
                        ), fg="red"
                    ),
                    click.style(
                        re.sub(
                            r'\B(?=(\d{3})+(?!\d))', ',',
                            str(item["recovered"]
                                ) if item["recovered"] is not None else "N/A"
                        ), fg="green"
                    ),
                    click.style(
                        str(item["latitude"]
                            ) if item["latitude"] is not None else 'N/A',
                        fg="cyan"
                    ),
                    click.style(
                        str(item["longitude"]
                            ) if item["longitude"] is not None else 'N/A',
                        fg="cyan"
                    ),
                    click.style(
                        str(
                            datetime.datetime.fromtimestamp(
                                item["last_update"] / 1000
                            ).strftime(
                                "%d-%m-%Y %H:%M:%S"
                            ) if item["last_update"] is not None else 'N/A'
                        ), fg="cyan"
                    )
                )
            )

    return tabulate.tabulate(data, headers=[
        click.style("Rank", fg="blue", underline=True),
        click.style("Id", fg="cyan", underline=True),
        click.style("Country", fg="bright_blue", underline=True),
        click.style("Confirmed", fg="yellow", underline=True),
        click.style("Active", fg="magenta", underline=True),
        click.style("Deaths", fg="red", underline=True),
        click.style("Recovered", fg="green", underline=True),
        click.style("Latitude", fg="cyan",
                    underline=True) if verbose else None,
        click.style("Longitude", fg="cyan",
                    underline=True) if verbose else None,
        click.style("Last Update", fg="cyan",
                    underline=True) if verbose else None,
    ], tablefmt="pretty")


# Helper for `list-countries`
def __listCountries() -> str:
    covid_data = covid.Covid()
    i = 0
    countries = []
    for country in covid_data.list_countries():
        i += 1
        countries.append(
            (
                click.style(str(i), fg="cyan"),
                click.style(str(country["id"]), fg="blue"),
                click.style(str(country["name"]), fg="green")
            )
        )
    return tabulate.tabulate(countries, headers=[
        click.style("Rank", fg="cyan", underline=True),
        click.style("Id", fg="blue", underline=True),
        click.style("Name", fg="green", underline=True)
    ], tablefmt="pretty")


# Helper for `country-id`
def __getStatsById(verbose: bool, id: int) -> str:
    covid_data = covid.Covid()
    data = []
    country_data = covid_data.get_status_by_country_id(id)
    all_country_data = covid_data.get_data()
    all_country_ids = [int(item["id"]) for item in all_country_data]
    rank = click.style(str(all_country_ids.index(id) + 1), fg="blue")
    country_id = click.style(str(country_data["id"]), fg="cyan")
    country = click.style(str(country_data["country"]), fg="bright_blue")
    confirmed = click.style(
        re.sub(
            r'\B(?=(\d{3})+(?!\d))', ',',
            str(country_data["confirmed"])
        ) if country_data["confirmed"] is not None else 'N/A',
        fg="yellow"
    )
    active = click.style(
        re.sub(
            r'\B(?=(\d{3})+(?!\d))', ',',
            str(country_data["active"])
        ) if country_data["active"] is not None else 'N/A',
        fg="magenta"
    )
    deaths = click.style(
        re.sub(
            r'\B(?=(\d{3})+(?!\d))', ',',
            str(country_data["deaths"])
        ) if country_data["deaths"] is not None else 'N/A',
        fg="red"
    )
    recovered = click.style(
        re.sub(
            r'\B(?=(\d{3})+(?!\d))', ',',
            str(country_data["recovered"])
        ) if country_data["recovered"] is not None else 'N/A',
        fg="green"
    )
    latitude = click.style(
        str(country_data["latitude"]
            ) if country_data["latitude"] is not None else 'N/A',
        fg="cyan"
    )
    longitude = click.style(
        str(country_data["longitude"]
            ) if country_data["longitude"] is not None else 'N/A',
        fg="cyan"
    )
    last_update = click.style(
        str(
            datetime.datetime.fromtimestamp(
                country_data["last_update"] / 1000
            ).strftime(
                "%d-%m-%Y %H:%M:%S"
            ) if country_data["last_update"] is not None else 'N/A'
        ), fg="cyan"
    )
    if verbose:
        data.append(
            (
                rank,
                country_id,
                country,
                confirmed,
                active,
                deaths,
                recovered,
                latitude,
                longitude,
                last_update
            )
        )
        table = tabulate.tabulate(
            data,
            headers=[
                click.style("Rank", fg="blue", underline=True),
                click.style("Id", fg="cyan", underline=True),
                click.style("Country", fg="bright_blue", underline=True),
                click.style("Confirmed", fg="yellow", underline=True),
                click.style("Active", fg="magenta", underline=True),
                click.style("Deaths", fg="red", underline=True),
                click.style("Recovered", fg="green", underline=True),
                click.style("Latitude", fg="cyan", underline=True),
                click.style("Longitude", fg="cyan", underline=True),
                click.style("Last Update", fg="cyan", underline=True)
            ],
            tablefmt="pretty"
        )
    else:
        data.append(
            (
                rank,
                country_id,
                country,
                confirmed,
                active,
                deaths,
                recovered
            )
        )
        table = tabulate.tabulate(
            data,
            headers=[
                click.style("Rank", fg="blue", underline=True),
                click.style("Id", fg="cyan", underline=True),
                click.style("Country", fg="bright_blue", underline=True),
                click.style("Confirmed", fg="yellow", underline=True),
                click.style("Active", fg="magenta", underline=True),
                click.style("Deaths", fg="red", underline=True),
                click.style("Recovered", fg="green", underline=True)
            ],
            tablefmt="pretty"
        )
    return table


# Helper for `country-name`
def __getStatsByName(verbose: bool, name: str) -> str:
    covid_data = covid.Covid()
    data = []
    country_data = covid_data.get_status_by_country_name(name)
    all_country_data = covid_data.get_data()
    all_country_names = [str(item["country"]) for item in all_country_data]
    rank = click.style(str(all_country_names.index(name) + 1), fg="blue")
    country_id = click.style(str(country_data["id"]), fg="cyan")
    country = click.style(str(country_data["country"]), fg="bright_blue")
    confirmed = click.style(
        re.sub(
            r'\B(?=(\d{3})+(?!\d))', ',',
            str(country_data["confirmed"])
        ) if country_data["confirmed"] is not None else 'N/A',
        fg="yellow"
    )
    active = click.style(
        re.sub(
            r'\B(?=(\d{3})+(?!\d))', ',',
            str(country_data["active"])
        ) if country_data["active"] is not None else 'N/A',
        fg="magenta"
    )
    deaths = click.style(
        re.sub(
            r'\B(?=(\d{3})+(?!\d))', ',',
            str(country_data["deaths"])
        ) if country_data["deaths"] is not None else 'N/A',
        fg="red"
    )
    recovered = click.style(
        re.sub(
            r'\B(?=(\d{3})+(?!\d))', ',',
            str(country_data["recovered"])
        ) if country_data["recovered"] is not None else 'N/A',
        fg="green"
    )
    latitude = click.style(
        str(country_data["latitude"]
            ) if country_data["latitude"] is not None else 'N/A',
        fg="cyan"
    )
    longitude = click.style(
        str(country_data["longitude"]
            ) if country_data["longitude"] is not None else 'N/A',
        fg="cyan"
    )
    last_update = click.style(
        str(
            datetime.datetime.fromtimestamp(
                country_data["last_update"] / 1000
            ).strftime(
                "%d-%m-%Y %H:%M:%S"
            ) if country_data["last_update"] is not None else 'N/A'
        ), fg="cyan"
    )
    if verbose:
        data.append(
            (
                rank,
                country_id,
                country,
                confirmed,
                active,
                deaths,
                recovered,
                latitude,
                longitude,
                last_update
            )
        )
        table = tabulate.tabulate(
            data,
            headers=[
                click.style("Rank", fg="blue", underline=True),
                click.style("Id", fg="cyan", underline=True),
                click.style("Country", fg="bright_blue", underline=True),
                click.style("Confirmed", fg="yellow", underline=True),
                click.style("Active", fg="magenta", underline=True),
                click.style("Deaths", fg="red", underline=True),
                click.style("Recovered", fg="green", underline=True),
                click.style("Latitude", fg="cyan", underline=True),
                click.style("Longitude", fg="cyan", underline=True),
                click.style("Last Update", fg="cyan", underline=True)
            ],
            tablefmt="pretty"
        )
    else:
        data.append(
            (
                rank,
                country_id,
                country,
                confirmed,
                active,
                deaths,
                recovered
            )
        )
        table = tabulate.tabulate(
            data,
            headers=[
                click.style("Rank", fg="blue", underline=True),
                click.style("Id", fg="cyan", underline=True),
                click.style("Country", fg="bright_blue", underline=True),
                click.style("Confirmed", fg="yellow", underline=True),
                click.style("Active", fg="magenta", underline=True),
                click.style("Deaths", fg="red", underline=True),
                click.style("Recovered", fg="green", underline=True)
            ],
            tablefmt="pretty"
        )
    return table


# Helper for `country-rank`
def __getStatusByRank(verbose: bool, rank: int) -> str:
    covid_data = covid.Covid()
    data = []
    all_country_data = covid_data.get_data()
    country_data = all_country_data[rank - 1]
    rank = click.style(str(rank), fg="blue")
    country_id = click.style(str(country_data["id"]), fg="cyan")
    country = click.style(str(country_data["country"]), fg="bright_blue")
    confirmed = click.style(
        re.sub(
            r'\B(?=(\d{3})+(?!\d))', ',',
            str(country_data["confirmed"])
        ) if country_data["confirmed"] is not None else 'N/A',
        fg="yellow"
    )
    active = click.style(
        re.sub(
            r'\B(?=(\d{3})+(?!\d))', ',',
            str(country_data["active"])
        ) if country_data["active"] is not None else 'N/A',
        fg="magenta"
    )
    deaths = click.style(
        re.sub(
            r'\B(?=(\d{3})+(?!\d))', ',',
            str(country_data["deaths"])
        ) if country_data["deaths"] is not None else 'N/A',
        fg="red"
    )
    recovered = click.style(
        re.sub(
            r'\B(?=(\d{3})+(?!\d))', ',',
            str(country_data["recovered"])
        ) if country_data["recovered"] is not None else 'N/A',
        fg="green"
    )
    latitude = click.style(
        str(country_data["latitude"]
            ) if country_data["latitude"] is not None else 'N/A',
        fg="cyan"
    )
    longitude = click.style(
        str(country_data["longitude"]
            ) if country_data["longitude"] is not None else 'N/A',
        fg="cyan"
    )
    last_update = click.style(
        str(
            datetime.datetime.fromtimestamp(
                country_data["last_update"] / 1000
            ).strftime(
                "%d-%m-%Y %H:%M:%S"
            ) if country_data["last_update"] is not None else 'N/A'
        ), fg="cyan"
    )
    if verbose:
        data.append(
            (
                rank,
                country_id,
                country,
                confirmed,
                active,
                deaths,
                recovered,
                latitude,
                longitude,
                last_update
            )
        )
        table = tabulate.tabulate(
            data,
            headers=[
                click.style("Rank", fg="blue", underline=True),
                click.style("Id", fg="cyan", underline=True),
                click.style("Country", fg="bright_blue", underline=True),
                click.style("Confirmed", fg="yellow", underline=True),
                click.style("Active", fg="magenta", underline=True),
                click.style("Deaths", fg="red", underline=True),
                click.style("Recovered", fg="green", underline=True),
                click.style("Latitude", fg="cyan", underline=True),
                click.style("Longitude", fg="cyan", underline=True),
                click.style("Last Update", fg="cyan", underline=True)
            ],
            tablefmt="pretty"
        )
    else:
        data.append(
            (
                rank,
                country_id,
                country,
                confirmed,
                active,
                deaths,
                recovered
            )
        )
        table = tabulate.tabulate(
            data,
            headers=[
                click.style("Rank", fg="blue", underline=True),
                click.style("Id", fg="cyan", underline=True),
                click.style("Country", fg="bright_blue", underline=True),
                click.style("Confirmed", fg="yellow", underline=True),
                click.style("Active", fg="magenta", underline=True),
                click.style("Deaths", fg="red", underline=True),
                click.style("Recovered", fg="green", underline=True)
            ],
            tablefmt="pretty"
        )
    return table


# Helper for `confirmed`
def __getTotalConfirmedCases():
    covid_data = covid.Covid()
    data = re.sub(r'\B(?=(\d{3})+(?!\d))', ',',
                  str(covid_data.get_total_confirmed_cases()))
    return tabulate.tabulate(
        [
            (click.style(data, fg="yellow"),)
        ], headers=[
            click.style("Confirmed", fg="yellow", underline=True)
        ], tablefmt="pretty"
    )


# Helper for `active`
def __getTotalActiveCases():
    covid_data = covid.Covid()
    data = re.sub(r'\B(?=(\d{3})+(?!\d))', ',',
                  str(covid_data.get_total_active_cases()))
    return tabulate.tabulate(
        [
            (click.style(data, fg="magenta"),)
        ], headers=[
            click.style("Active", fg="magenta", underline=True)
        ], tablefmt="pretty"
    )


# Helper for `deaths`
def __getTotalDeaths():
    covid_data = covid.Covid()
    data = re.sub(r'\B(?=(\d{3})+(?!\d))', ',',
                  str(covid_data.get_total_deaths()))
    return tabulate.tabulate(
        [
            (click.style(data, fg="red"),)
        ], headers=[
            click.style("Deaths", fg="red", underline=True)
        ], tablefmt="pretty"
    )


# Helper for `recovered`
def __getTotalRecovered():
    covid_data = covid.Covid()
    data = re.sub(r'\B(?=(\d{3})+(?!\d))', ',',
                  str(covid_data.get_total_recovered()))
    return tabulate.tabulate(
        [
            (click.style(data, fg="green"),)
        ], headers=[
            click.style("Recovered", fg="green", underline=True)
        ], tablefmt="pretty"
    )


# Helper for `total`
def __getTotal():
    covid_data = covid.Covid()
    confirmed = re.sub(r'\B(?=(\d{3})+(?!\d))', ',',
                       str(covid_data.get_total_confirmed_cases()))
    active = re.sub(r'\B(?=(\d{3})+(?!\d))', ',',
                    str(covid_data.get_total_active_cases()))
    deaths = re.sub(r'\B(?=(\d{3})+(?!\d))', ',',
                    str(covid_data.get_total_deaths()))
    recovered = re.sub(r'\B(?=(\d{3})+(?!\d))', ',',
                       str(covid_data.get_total_recovered()))
    data = [
        (
            click.style(confirmed, fg="yellow"),
            click.style(active, fg="magenta"),
            click.style(deaths, fg="red"),
            click.style(recovered, fg="green"),
        )
    ]

    return tabulate.tabulate(data, headers=[
        click.style("Confirmed", fg="yellow"),
        click.style("Active", fg="magenta"),
        click.style("Deaths", fg="red"),
        click.style("Recovered", fg="green")
    ], tablefmt="pretty")


@click.group(
    cls=click_help_colors.HelpColorsGroup,
    help_headers_color='yellow',
    help_options_color='green',
    help=app_description
)
@click.version_option(app_version, '-V', '--version', prog_name=app_name)
@click.help_option('-h', '--help')
def covistats():
    pass


@covistats.command(
    cls=click_help_colors.HelpColorsCommand,
    help="Show statistics of all countries."
)
@click.option('-v', '--verbose', is_flag=True, help="Enable verbose mode.")
@click.help_option('-h', '--help')
def all_data(verbose: bool):
    try:
        with click_spinner.spinner():
            data = __getAllCountriesData(verbose)
        click.echo(data)
    except Exception as e:
        raise click.ClickException(e)


@covistats.command(
    cls=click_help_colors.HelpColorsCommand,
    help="List all available countries."
)
@click.option(
    '-v', '--verbose', is_flag=True,
    help="Enable verbose mode (same as 'covistats all-data')."
)
@click.help_option('-h', '--help')
@click.pass_context
def list_countries(context: click.core.Context, verbose: bool):
    try:
        if verbose:
            context.invoke(all_data)
        else:
            with click_spinner.spinner():
                data = __listCountries()
            click.echo(data)
    except Exception as e:
        raise click.ClickException(e)


@covistats.command(
    cls=click_help_colors.HelpColorsCommand,
    help="Get statistics of given country id \
(run 'covistats list-countries' to get a list of available countries and ids)"
)
@click.option(
    '-v', '--verbose', is_flag=True,
    help="Enable verbose mode."
)
@click.argument('id', type=int)
@click.help_option('-h', '--help')
def country_id(verbose: bool, id: int):
    try:
        with click_spinner.spinner():
            data = __getStatsById(verbose, id)
        click.echo(data)
    except Exception as e:
        raise click.ClickException(e)


@covistats.command(
    cls=click_help_colors.HelpColorsCommand,
    help="Get statistics of given country \
(run 'covistats list-countries' to get a list of available countries and ids)"
)
@click.option(
    '-v', '--verbose', is_flag=True,
    help="Enable verbose mode."
)
@click.argument('name', type=str)
@click.help_option('-h', '--help')
def country_name(verbose: bool, name: int):
    try:
        with click_spinner.spinner():
            data = __getStatsByName(verbose, name)
        click.echo(data)
    except Exception as e:
        raise click.ClickException(e)


@covistats.command(
    cls=click_help_colors.HelpColorsCommand,
    help="Get statistics of the country of the given rank."
)
@click.option(
    '-v', '--verbose', is_flag=True,
    help="Enable verbose mode."
)
@click.argument('rank', type=int)
@click.help_option('-h', '--help')
def country_rank(verbose: bool, rank: int):
    try:
        with click_spinner.spinner():
            data = __getStatusByRank(verbose, rank)
        click.echo(data)
    except Exception as e:
        raise click.ClickException(e)


@covistats.command(
    cls=click_help_colors.HelpColorsCommand,
    help="Get total confirmed cases."
)
@click.help_option('-h', '--help')
def confirmed():
    try:
        with click_spinner.spinner():
            data = __getTotalConfirmedCases()
        click.echo(data)
    except Exception as e:
        raise click.ClickException(e)


@covistats.command(
    cls=click_help_colors.HelpColorsCommand,
    help="Get total active cases."
)
@click.help_option('-h', '--help')
def active():
    try:
        with click_spinner.spinner():
            data = __getTotalActiveCases()
        click.echo(data)
    except Exception as e:
        raise click.ClickException(e)


@covistats.command(
    cls=click_help_colors.HelpColorsCommand,
    help="Get total deaths."
)
@click.help_option('-h', '--help')
def deaths():
    try:
        with click_spinner.spinner():
            data = __getTotalDeaths()
        click.echo(data)
    except Exception as e:
        raise click.ClickException(e)


@covistats.command(
    cls=click_help_colors.HelpColorsCommand,
    help="Get number of total recovered patients."
)
@click.help_option('-h', '--help')
def recovered():
    try:
        with click_spinner.spinner():
            data = __getTotalRecovered()
        click.echo(data)
    except Exception as e:
        raise click.ClickException(e)


@covistats.command(
    cls=click_help_colors.HelpColorsCommand,
    help="Get number of total confirmed cases, active cases, deaths \
and recovered patients."
)
@click.help_option('-h', '--help')
def total():
    try:
        with click_spinner.spinner():
            data = __getTotal()
        click.echo(data)
    except Exception as e:
        raise click.ClickException(e)


if __name__ == "__main__":
    covistats(prog_name=app_name.lower())
