# -*- coding: utf-8 -*-

import logging
import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import dashboardLayout
import utils
from datetime import date


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SIMPLEX])
server = app.server
app.layout = html.Div(
    [
        dcc.Location(
            id="url",
            refresh=False
        ),
        html.Div(
            id="page-content"
        ),
        dashboardLayout.create_layout()
    ]
)

######################################### CALLBACK DEFINITONS #########################################


@app.callback(
    [
        Output(dashboardLayout.REGIONS_DROPDOWN_ID, 'options'),
        Output(dashboardLayout.REGIONS_DROPDOWN_DIV_LOADING, 'children')
    ],
    Input(dashboardLayout.PROVINCES_DROPDOWN_ID, 'value'),
    prevent_initial_call=True
)
def set_regions_options(province):
    return utils.get_regions_options(province), dash.no_update


@app.callback(
    Output(dashboardLayout.REGIONS_DROPDOWN_ID, 'value'),
    Input(dashboardLayout.REGIONS_DROPDOWN_ID, 'options'),
    prevent_initial_call=True
)
def set_regions_value(options):
    return options[0]['value']


@app.callback(
    [
        Output('cases', 'children'),
        Output('cases-today', 'children'),
        Output('active_cases', 'children'),
        Output('active_cases-today', 'children'),
        Output('deaths', 'children'),
        Output('deaths-today', 'children'),
        # Output('hospitalized', 'children'),
        # Output('hospitalized-today', 'children'),
        # Output('hospitalized_critical', 'children'),
        # Output('hospitalized_critical-today', 'children'),
        Output('recoveries', 'children'),
        Output('recoveries-today', 'children'),
        Output('tests', 'children'),
        Output('tests-today', 'children'),
        Output('vaccinated', 'children'),
        Output('vaccinated-today', 'children'),
    ],
    [
        Input('load-button', 'n_clicks')
    ],
    [
        State(dashboardLayout.PROVINCES_DROPDOWN_ID, 'value'),
        State(dashboardLayout.REGIONS_DROPDOWN_ID, 'value'),
    ],
    prevent_initial_call=True
)
def update_stats(n, province, health_region):
    print("Province: {}, Health Region: {}".format(province, health_region))
    if province is 'RP' or health_region is 9999:
        error_msg = "Querying for province code {} and/or health_region " \
            "code {} is not supported".format(province, health_region)
        # TODO this is not being displayed
    location = None
    if health_region is 0:
        location = province
    else:
        location = health_region
    today_date = date.today().strftime("%d-%m-%y")
    summary_data = utils.get_summary(location, today_date)
    utils.jprint(summary_data)
    cases_str = "{} cases".format(
        utils.get_summary_dict_value(summary_data, "cumulative_cases"))
    cases_today_str = "{} today".format(
        utils.get_summary_dict_value(summary_data, "cases"))
    active_cases_str = "{} active cases".format(
        utils.get_summary_dict_value(summary_data, "active_cases"))
    active_cases_today_str = "{} today".format(
        utils.get_summary_dict_value(summary_data, "active_cases_change"))
    deaths_str = "{} deaths".format(
        utils.get_summary_dict_value(summary_data, "cumulative_deaths"))
    deaths_today_str = "{} today".format(
        utils.get_summary_dict_value(summary_data, "deaths"))
    recoveries_str = "{} recoveries".format(
        utils.get_summary_dict_value(summary_data, "cumulative_recovered"))
    recoveries_today_str = "{} today".format(
        utils.get_summary_dict_value(summary_data, "recovered"))
    tests_str = "{} tests".format(
        utils.get_summary_dict_value(summary_data, "cumulative_testing"))
    tests_today_str = "{} today".format(
        utils.get_summary_dict_value(summary_data, "testing"))
    vaccinated_str = "{} vaccinated".format(
        utils.get_summary_dict_value(summary_data, "cumulative_avaccine"))
    vaccinated_today_str = "{} today".format(
        utils.get_summary_dict_value(summary_data, "avaccine"))
        
    return [
        cases_str,
        cases_today_str,
        active_cases_str,
        active_cases_today_str,
        deaths_str,
        deaths_today_str,
        recoveries_str,
        recoveries_today_str,
        tests_str,
        tests_today_str,
        vaccinated_str,
        vaccinated_today_str,
    ]


if __name__ == "__main__":
    app.run_server(debug=True)
