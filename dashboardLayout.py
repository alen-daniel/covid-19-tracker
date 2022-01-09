import dash_bootstrap_components as dbc
from dash import html
from dash import dcc

REGIONAL_DROPDOWN_ID = "region-dropdown"
PROVINCE_DROPDOWN_ID = "province-dropdown"


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


def create_layout(province_dropdown_dict):
    return dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.H6("Select Province"),
                            dcc.Dropdown(
                                id=PROVINCE_DROPDOWN_ID,
                                options=province_dropdown_dict,
                                # value=province_dropdown_dict[0]["value"]
                            )
                        ],
                        width=3
                    ),
                    dbc.Col(
                        [
                            html.H6("Select Province"),
                            # html.Div(id=REGIONAL_DROPDOWN_ID),
                            dcc.Dropdown(
                                id=REGIONAL_DROPDOWN_ID,
                                options=[],
                                # value=province_dropdown_dict[0]["value"]
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
