import dash_bootstrap_components as dbc
from dash import html
from dash import dcc
import utils

REGIONS_DROPDOWN_ID = "region-dropdown"
PROVINCES_DROPDOWN_ID = "province-dropdown"
REGIONS_DROPDOWN_DIV_LOADING = REGIONS_DROPDOWN_ID + "-loading-div"


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
    province_options = utils.get_province_options()
    region_options = utils.get_regions_options("ALL")
    return dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.H6("Select Province"),
                            dcc.Dropdown(
                                id=PROVINCES_DROPDOWN_ID,
                                options=province_options,
                                value=province_options[0]["value"]
                            )
                        ],
                        width=2
                    ),
                    dbc.Col(
                        [
                            html.H6("Select Health Region"),
                            dcc.Loading(
                                children=[
                                    html.Div(id=REGIONS_DROPDOWN_DIV_LOADING),
                                    dcc.Dropdown(
                                        id=REGIONS_DROPDOWN_ID,
                                        options=region_options,
                                        value=region_options[0]["value"]
                                    ),
                                ]
                            )
                        ],
                        width=4
                    ),
                    dbc.Col(
                        [
                            dbc.Button(
                                "Load Graphs",
                                id="load-button",
                                className="me-2",
                                n_clicks=0,
                            ),
                        ],
                        width=3
                    ),
                ],
                align='start',
            ),
            # dbc.Row(
            #     [
            #         create_stats_column("cases"),
            #         create_stats_column("cases-active"),
            #         create_stats_column("deaths"),
            #         create_stats_column("hospitalized"),
            #         create_stats_column("hospitalized-critical"),
            #         create_stats_column("recoveries"),
            #         create_stats_column("tests"),
            #         create_stats_column("vaccinated"),
            #         create_stats_column("active-cases"),
            #         create_stats_column("active-cases"),
            #     ],
            # ),
        ],
        fluid=True
    )
