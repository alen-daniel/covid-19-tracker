import dash_bootstrap_components as dbc
from dash import html
from dash import dcc
import utils

REGIONAL_DROPDOWN_ID = "region-dropdown"
PROVINCE_DROPDOWN_ID = "province-dropdown"
REGIONAL_DROPDOWN_DIV_LOADING = REGIONAL_DROPDOWN_ID + "-loading-div"


def create_stats_column(name):
    return dbc.Col(
        [
            dbc.Row(
                [
                    dbc.Col(html.Div(str(name))),
                ]
            ),
            dbc.Row(
                [
                    dbc.Col(html.Div(str(name) + "-today")),
                ]
            )
        ]
    )


def create_layout():
    return dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.H6("Select Province"),
                            dcc.Dropdown(
                                id=PROVINCE_DROPDOWN_ID,
                                options=utils.get_province_list(),
                                # value=province_dropdown_dict[0]["value"]
                            )
                        ],
                        width=3
                    ),
                    dbc.Col(
                        [
                            html.H6("Select Health Region"),
                            dcc.Loading(
                                children=[
                                    html.Div(id=REGIONAL_DROPDOWN_DIV_LOADING),
                                    dcc.Dropdown(
                                        id=REGIONAL_DROPDOWN_ID,
                                        options=[]),
                                    # value=province_dropdown_dict[0]["value"]
                                ]
                            )
                        ],
                        width=3
                    )
                ],
                align='start',
            ),
            dbc.Row(
                [
                    create_stats_column("cases"),
                    create_stats_column("cases-active"),
                    create_stats_column("deaths"),
                    create_stats_column("hospitalized"),
                    create_stats_column("hospitalized-critical"),
                    create_stats_column("recoveries"),
                    create_stats_column("tests"),
                    create_stats_column("vaccinated"),
                    create_stats_column("active-cases"),
                    create_stats_column("active-cases"),
                ]
            ),
        ],
        fluid=True
    )
