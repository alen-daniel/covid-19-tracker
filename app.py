# -*- coding: utf-8 -*-

import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import dashboardLayout
import requests
import json


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


def get_province_list():
    prov_query_url = "https://api.opencovid.ca/other?stat=prov"
    response = requests.get(prov_query_url)
    print("Querying province list. Return status code: {}".format(
        response.status_code))
    if response.status_code is not 200:
        return []  # TODO
    response_json = response.json()
    result_dict_list = []
    for prov in response_json["prov"]:
        result_dict = {}
        result_dict["label"] = prov["province_full"]
        result_dict["value"] = prov["province_short"]
        result_dict_list.append(result_dict)
    return result_dict_list


def get_regions_options(province):
    hr_query_url = "https://api.opencovid.ca/other?stat=hr"
    response = requests.get(hr_query_url)
    print("Querying Health Regions list. Return status code: {}".format(
        response.status_code))
    if response.status_code is not 200:
        return []  # TODO
    response_json = response.json()
    result_dict_list = []
    for region in response_json["hr"]:
        if region["province_short"] != str(province):
            continue
        result_dict = {}
        result_dict["label"] = region["health_region_esri"]
        result_dict["value"] = region["HR_UID"]
        result_dict_list.append(result_dict)
    return result_dict_list


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
        dashboardLayout.create_layout(get_province_list())
    ]
)


######################################### CALLBACK DEFINITONS #########################################

# @app.callback(
#     [
#         Output(dashboardLayout.REGIONAL_DROPDOWN_ID, "children")
#     ],
#     [
#         Input("province-dropdown", "value")
#     ],
#     prevent_initial_call=True
# )
# def populate_regional_dropdown(province):
#     get_region_dict_list = get_region_list(province)
#     return dcc.Dropdown(
#         options=get_region_dict_list,
#         # value=get_region_dict_list[0]["value"]
#     )

@app.callback(
    Output(dashboardLayout.REGIONAL_DROPDOWN_ID, "options"),
    Input(dashboardLayout.PROVINCE_DROPDOWN_ID, 'value'),
    prevent_initial_call=True
)
def set_regions_options(province):
    return get_regions_options(province)

# @app.callback(
#     Output(dashboardLayout.REGIONAL_DROPDOWN_ID, 'value'),
#     Input(dashboardLayout.REGIONAL_DROPDOWN_ID, 'options'),
#     prevent_initial_call=True
# )
# def set_regions_value(available_options):
#     return available_options[0]['value']


if __name__ == "__main__":
    app.run_server(debug=True)
