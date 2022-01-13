# -*- coding: utf-8 -*-

import dash_bootstrap_components as dbc
from dash import html
from dash import dcc
import utils

REGIONS_DROPDOWN_ID = "region-dropdown"
PROVINCES_DROPDOWN_ID = "province-dropdown"
REGIONS_DROPDOWN_DIV_LOADING = REGIONS_DROPDOWN_ID + "-loading-div"


def create_stats_column(descriptor):
    return dbc.Col(
        [
            dbc.Card(
                [
                    html.H4(
                        descriptor,
                        id=descriptor,
                        className="card-title"
                    ),
                    html.H6(
                        descriptor + '-today',
                        id=descriptor + '-today',
                        className="card-subtitle"
                    ),
                ],
                body=True
            )
        ],
        width=3,
        align='center'
    )


def create_tracker_layout():
    province_options = utils.get_province_options()
    region_options = utils.get_regions_options("ALL")
    return dbc.Container(
        [
            dbc.Card(
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
                                            html.Div(
                                                id=REGIONS_DROPDOWN_DIV_LOADING),
                                            dcc.Dropdown(
                                                id=REGIONS_DROPDOWN_ID,
                                                options=region_options,
                                                value=region_options[0]["value"]
                                            ),
                                        ]
                                    )
                                ],
                                width=4,
                            ),
                            dbc.Col(
                                [
                                    dbc.Button(
                                        "Get Data",
                                        id="load-button",
                                        color="light",
                                        className="me-1",
                                        n_clicks=0,
                                    ),
                                ],
                                width=4,
                                align='end',

                            ),
                        ],
                        justify='center',
                    ),
                ],
                body=True
            ),
            dbc.Row(
                [
                    create_stats_column("cases"),
                    create_stats_column("active_cases"),
                    create_stats_column("deaths"),
                    create_stats_column("recoveries"),
                    create_stats_column("tests"),
                    create_stats_column("vaccinated"),
                ],
                justify='center'
            ),
        ],
        fluid=True
    )
