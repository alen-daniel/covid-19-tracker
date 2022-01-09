# -*- coding: utf-8 -*-

import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
import dashboardLayout

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SIMPLEX])
server = app.server
app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")])

######################################### CALLBACK DEFINITONS #########################################
@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def display_page(pathname):
    return dashboardLayout.create_layout()


if __name__ == "__main__":
    app.run_server(debug=True)
