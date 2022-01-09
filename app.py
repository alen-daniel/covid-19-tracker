# -*- coding: utf-8 -*-

import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import dashboardLayout
import utils

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SIMPLEX])
server = app.server
app.layout = html.Div(
    [
        dcc.Location(
            id="url",
            refresh=False
        ),
        # html.Div(
        #     id="page-content"
        # )
        dashboardLayout.create_layout()
    ]
)

######################################### CALLBACK DEFINITONS #########################################

@app.callback(
    [
        Output(dashboardLayout.REGIONAL_DROPDOWN_ID, "options"),
        Output(dashboardLayout.REGIONAL_DROPDOWN_DIV_LOADING, "children")
    ],
    Input(dashboardLayout.PROVINCE_DROPDOWN_ID, 'value'),
    prevent_initial_call=True
)
def set_regions_options(province):
    return utils.get_regions_options(province), dash.no_update

if __name__ == "__main__":
    app.run_server(debug=True)
